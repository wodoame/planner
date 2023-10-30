from django.shortcuts import render, redirect
from .models import Task, Label
from datetime import datetime, timedelta
from .forms import CreateTask, EditTask
from django.contrib import messages

def index(request):
    # referer = request.META.get('HTTP_REFERER')
    # print(referer, '/delete-task' in referer)
    # if referer:
    #     if '/delete-task' in referer: 
    #         messages.success(request, 'task deleted successfully')
    today = []
    tomorrow = []
    upcoming = []
    expired = []
    # Task.objects.filter(label__title__in=['Education', 'Personal'])
    for task in Task.objects.all(): 
        dateToday = datetime.today().date()
        dateTomorrow = dateToday + timedelta(days=1)
        taskDate = task.deadline.date()
        if taskDate == dateToday: 
            today.append(task)
        elif taskDate == dateTomorrow: 
            tomorrow.append(task)
        elif taskDate > dateTomorrow: 
            upcoming.append(task)    
        else: 
            expired.append(task)

    context = {'today': today, 'upcoming':upcoming, 'tomorrow':tomorrow, 'expired': expired}
    return render(request,'core/index.html', context)

def createTask(request):
    initialData = {'label':Label.objects.first()}
    form = CreateTask(initial=initialData)
    if request.method == 'POST': 
        form = CreateTask(request.POST)
        if form.is_valid(): 
            task = form.save(commit=False)
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            parsed = datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M:%S')
            task.deadline = parsed
            form.save()
            messages.success(request, 'task created successfully')
            return redirect('index')
        else: 
            print(form.errors)
    context = {'form': form}
    return render(request, 'core/create-task.html', context)

def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, 'task deleted successfully')
    return redirect('index')

def editTask(request, id): 
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = EditTask(request.POST, instance=task)
        if form.is_valid(): 
            task = form.save(commit=False)
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            if date and time:
                parsed = datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M:%S')
                task.deadline = parsed
            form.save()
            messages.success(request, 'task edited successfully')
            return redirect('index')
        else: 
            print(form.errors)
    form = EditTask(instance=task)
    context = {'form':form, 'task': task}
    return render(request, 'core/edit-task.html', context)
    