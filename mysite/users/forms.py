from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This is how you inherit
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default is required = true

    # This class Meta is created to inform which model will interact witht he form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # password and confirm password
