from django.shortcuts import render
from . forms import TaskForm

# Create your views here.
from django.shortcuts import render, redirect
from . models import Task


def TaskList(request):
    tasks = Task.objects.all()
    return render(request, 'TodoList/TaskForm.html', {'tasks': tasks})

def CreateTask(request):
    tasks = Task.objects.filter(status = "pending")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect("create_task")
    else:
        form = TaskForm()

    return render(request, "TodoList/TaskList.html", {"form": form, "tasks":tasks})

def DeleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("create_task")

def CompleteTask(request, task_id):
    task = Task.objects.get(id = task_id)
    task.status = "completed"
    task.save()
    return redirect("create_task")