from django.urls import path 
import core.views  as core_views
urlpatterns = [
    # path('', core_views.createTask, name='create-task'), 
    path('', core_views.index, name='index'), 
    path('create-task/', core_views.createTask, name='create-task')
]