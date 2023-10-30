from django.urls import path 
import core.views  as core_views
urlpatterns = [
    # path('', core_views.createTask, name='create-task'), 
    path('', core_views.index, name='index'), 
    path('create-task/', core_views.createTask, name='create-task'), 
    path('delete-task/<int:id>', core_views.deleteTask, name='delete-task'), 
    path('edit-task/<int:id>', core_views.editTask, name='edit-task')
]