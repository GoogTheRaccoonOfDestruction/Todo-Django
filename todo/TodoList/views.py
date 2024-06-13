from django.contrib import messages
from django.shortcuts import render
from . forms import TaskForm, RegisterForm

# Create your views here.
from django.shortcuts import render, redirect
from . models import Task
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


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

# Define a view function named login_view that handles user login.
def login_view(request):

    # Check if the request method is POST (i.e., form submission).
    if request.method == 'POST':
        # Create an instance of AuthenticationForm with the request and form data.
        form = AuthenticationForm(request, data=request.POST)

        # Check if the form is valid.
        if form.is_valid():
            # Retrieve username and password from the form's cleaned_data.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user using the provided username and password.
            user = authenticate(username=username, password=password)
            # If authentication is successful, log in the user.
            if user is not None:
                login(request, user)
                # Display a success message informing the user about successful login.
                messages.info(request, f"You are now logged in as {username}.")
                # Redirect the user to the task list page.
                return redirect('task_list')
            else:
                # Display an error message for invalid username or password.
                messages.error(request, "Invalid username or password.")

        else:
            # Display an error message for invalid form data.
            messages.error(request, "Invalid username or password.")

        # If the request method is not POST, create a new instance of AuthenticationForm.
    else:
        form = AuthenticationForm()
    # Render the login form template with the form instance.
    return render(request, 'TodoList/login.html', {'form': form})


def register(request):
    # Check if the request method is POST (i.e., form submission).
    if request.method == 'POST':
    # Create an instance of RegisterForm with the form data from the request.
        form = RegisterForm(request.POST)
    # Check if the form is valid.
        if form.is_valid():
    # Save the form to create a new user.
            user = form.save
    # Log in the newly registered user.
            login(request, user)
    # Display a success message for successful registration.
            messages.success(request, "Registration successful")
    # Redirect the user to the task list page.
            return redirect('task_list')

    # Display an error message for unsuccessful registration due to invalid information.
        else:
            messages.error(request, "Uncessful resgistration. Invalid information")

        # If the request method is not POST, create a new instance of RegisterForm.
    else:
        form = RegisterForm()

# Render the registration form template with the form instance.
        return render(request, 'TodoList/register.html',{'form' : form})


def DeleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("create_task")

def CompleteTask(request, task_id):
    task = Task.objects.get(id = task_id)
    task.status = "completed"
    task.save()
    return redirect("create_task")