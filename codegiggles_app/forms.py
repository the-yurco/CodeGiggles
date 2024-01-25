# codegiggles_app/forms.py
from django import forms
from .models import Snippet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'language', 'description']

