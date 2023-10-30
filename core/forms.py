from django.forms import ModelForm 
from .models import Task
from django import forms

class CreateTask(ModelForm):
    date = forms.DateField()
    time = forms.TimeField()
    
    class Meta: 
        model = Task 
        fields = '__all__'
        exclude = ['deadline']
        
class EditTask(CreateTask): 
    date = forms.DateField(required=False)
    time = forms.TimeField(required=False)

