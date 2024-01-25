# codegiggles_app/urls.py
from django.urls import path
from .views import home, snippets, add_snippet, snippet_detail, like, dislike, user_login, user_register, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('snippets/', snippets, name='snippets'),
    path('add_snippet/', add_snippet, name='add_snippet'),
    path('snippets/<int:snippet_id>/', snippet_detail, name='snippet_detail'),
    path('<int:snippet_id>/like/', like, name='like'),
    path('<int:snippet_id>/dislike/', dislike, name='dislike'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
