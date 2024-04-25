from django.shortcuts import render
from . forms import TaskForm

# Create your views here.
from django.shortcuts import render, redirect
from . models import Task


def TaskList(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.status = 'completed'
        task.save()
        return redirect('tasklist')
    else:
        tasks = Task.objects.filter(status='pending')
        return render(request, 'TodoList/TaskList.html', {'tasks': tasks})

def CreateTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect("tasklist")
    else:
        form = TaskForm()

    return render(request, "TodoList/TaskForm.html", {"form": form})