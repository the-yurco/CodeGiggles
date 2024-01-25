from django import forms
from .models import Snippet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'language', 'description']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User