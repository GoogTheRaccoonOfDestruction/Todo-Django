from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path("" ,views.TaskList, name="tasklist"),
    path("", views.CreateTask, name="create_task"),
    path("complete/<int:task_id>/" ,views.CompleteTask, name="completetask"),
    path("delete/<int:task_id>/", views.DeleteTask, name="deletetask"),
    ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

