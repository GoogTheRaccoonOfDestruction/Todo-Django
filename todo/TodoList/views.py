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

# Define a view function named login_view that handles user login.
def login_view(request):
    pass
    # Check if the request method is POST (i.e., form submission).

        # Create an instance of AuthenticationForm with the request and form data.

        # Check if the form is valid.

            # Retrieve username and password from the form's cleaned_data.

            # Authenticate the user using the provided username and password.

            # If authentication is successful, log in the user.

                # Display a success message informing the user about successful login.

                # Redirect the user to the task list page.


                # Display an error message for invalid username or password.


            # Display an error message for invalid form data.


        # If the request method is not POST, create a new instance of AuthenticationForm.

    # Render the login form template with the form instance.



def register(request):
    pass
    # Check if the request method is POST (i.e., form submission).

        # Create an instance of RegisterForm with the form data from the request.

        # Check if the form is valid.

            # Save the form to create a new user.

            # Log in the newly registered user.

            # Display a success message for successful registration.

            # Redirect the user to the task list page.


            # Display an error message for unsuccessful registration due to invalid information.


        # If the request method is not POST, create a new instance of RegisterForm.

    # Render the registration form template with the form instance.


def DeleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("create_task")

def CompleteTask(request, task_id):
    task = Task.objects.get(id = task_id)
    task.status = "completed"
    task.save()
    return redirect("create_task")