from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    pass


class Label(models.Model):
    label_titles = (
    ('Education', 'Education'), 
    ('Personal', 'Personal'), 
    ('Travel', 'Travel'), 
    ('Work', 'Work'), 
     )
    
    label_themes = (
    ('theme-1', 'blue theme'), 
    ('theme-2', 'purple theme'), 
    ('theme-3', 'orange theme'), 
    ('theme-4', 'green theme'), 
     )
    
    title = models.CharField(max_length=128, choices=label_titles)
    theme = models.CharField(max_length=128, choices=label_themes, null=True)
    
    def __str__(self) -> str:
        return self.title[:25] + '...'
    
    
class Task(models.Model): 
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, related_name='tasks', null=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    deadline = models.DateTimeField(null=True)
    status = models.CharField(max_length=128, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.title[:25] + '...'