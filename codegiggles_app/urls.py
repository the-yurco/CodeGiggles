# codegiggles_app/urls.py
from django.urls import path
from .views import home, snippets, add_snippet, snippet_detail, like, dislike

urlpatterns = [
    path('', home, name='home'),
    path('snippets/', snippets, name='snippets'),
    path('add_snippet/', add_snippet, name='add_snippet'),
    path('snippets/<int:snippet_id>/', snippet_detail, name='snippet_detail'),
    path('<int:snippet_id>/like/', like, name='like'),
    path('<int:snippet_id>/dislike/', dislike, name='dislike'),

]
