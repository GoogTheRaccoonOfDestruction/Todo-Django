from django.shortcuts import render
from . forms import TaskForm

# Create your views here.
from django.shortcuts import render, redirect
from . models import Task

def TaskList(request):
    tasks = Task.objects.all
    return render(request, "TodoList/TaskList.html", {"tasks":tasks})

def CreateTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect("tasklist")
    else:
        form = TaskForm()

    return render(request, "TodoList/TaskForm.html", {"form": form})