from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Snippet
from .forms import SnippetForm, UserRegistrationForm, UserLoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import logout


def home(request):
    snippets = Snippet.objects.all().order_by('-created_at')
    return render(request, 'codegiggles_app/home.html', {'snippets': snippets})

def snippets(request):
    query = request.GET.get('q')
    snippets = Snippet.objects.all().order_by('-created_at')

    if query:
        snippets = snippets.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(language__icontains=query) |
            Q(code__icontains=query)
        )

    context = {
        'snippets': snippets,
    }

    return render(request, 'codegiggles_app/snippets.html', context)

def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets')  
    else:
        form = SnippetForm()

    return render(request, 'codegiggles_app/add_snippet.html', {'form': form})

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'codegiggles_app/snippet_detail.html', {'snippet': snippet})

@login_required
def like(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    snippet.likes += 1
    snippet.save()
    
    data = {'likes': snippet.likes}
    return JsonResponse(data)

@login_required
def dislike(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    snippet.dislikes += 1
    snippet.save()

    data = {'dislikes': snippet.dislikes}
    return JsonResponse(data)

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'codegiggles_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'codegiggles_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
