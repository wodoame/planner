from django.shortcuts import render
from .models import Task
from datetime import datetime, timedelta
from django.db.models import Q 

def index(request):
    today = []
    tomorrow = []
    upcoming = []
    # Task.objects.filter(label__title__in=['Education', 'Personal'])
    for task in Task.objects.all(): 
        dateToday = datetime.today().date()
        if task.deadline.date() == dateToday: 
            today.append(task)
        elif task.deadline.date() == dateToday + timedelta(days=1): 
            tomorrow.append(task)
        else: 
            upcoming.append(task)    
    context = {'today': today, 'upcoming':upcoming, 'tomorrow':tomorrow}
    return render(request,'core/index.html', context)

    