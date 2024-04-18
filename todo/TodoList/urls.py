from django.urls import path
from . import views

urlpatterns = [
    path("" ,views.TaskList, name="tasklist"),
    path("create/", views.CreateTask, name="create_task"),
    ]