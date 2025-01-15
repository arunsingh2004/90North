from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use your custom User model
        fields = ['username', 'email', 'password1', 'password2']  # Specify fields
