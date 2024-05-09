from django.urls import path
from . import views

urlpatterns = [
    #path("" ,views.TaskList, name="tasklist"),
    path("", views.CreateTask, name="create_task"),
    path("complete/<int:task_id>/" ,views.CompleteTask, name="completetask"),
    path("delete/<int:task_id>/", views.DeleteTask, name="deletetask"),
    ]