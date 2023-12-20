# codegiggles_app/urls.py
from django.urls import path
from .views import home, snippets

urlpatterns = [
    path('', home, name='home'),
    path('snippets/', snippets, name='snippets'),
    path('add_snippet/', snippets, name='add_snippet'),
]
