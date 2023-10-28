from django.shortcuts import render
from .models import Task, Label
from datetime import datetime, timedelta
from .forms import CreateTask

def index(request):
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
            print(form.cleaned_data)
        else: 
            print(form.errors)
    context = {'form': form}
    return render(request, 'core/create-task.html', context)
    