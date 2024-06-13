from django import forms
from . models import Task


# Define a custom registration form that inherits from UserCreationForm
#
#     # Add an email field to the form (from forms grab the .EmailField() store it in variable called email
#
#
#
#     # Specify the model to be used for the form (User model)
#     '''
#     Define and inner class Meta with a variable named model as the User
#     you must import User form django.contrib.auth.models metadata for the form
#     '''
#
#
#         # Specify the fields to be included in the form username, email, password1, password2
#         '''
#         create a list called fields with the respective fields to represent each of the bit of information required to
#         register a user.
#         '''
#
#
#
# # CustomAuthenticationForm:
# #
# # Define a custom authentication form named CustomAuthenticationForm that inherits from Django's AuthenticationForm.
#
# # Define a form field for the username input
# # Define a form field for the password input
# '''
# create a username and password field for the login form, grab a .CharField from forms,
# generate a default widget value to that = to a .TextInput from forms, and a default attrs (attributes) field that's
# = a dictionary with two keys, class and placeholder and the value for
# class is form-control, and the value placeholder is Username and Password for password filed
# '''

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'type', 'priority']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        moder = User
        fields = ['username', 'email', 'password1', 'password2']