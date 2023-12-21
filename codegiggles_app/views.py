from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q


def home(request):
  #! latest 8 snippets
  snippets = Snippet.objects.all().order_by('-created_at')
  return render(request, 'codegiggles_app/home.html', {'snippets': snippets})
 
def snippets(request):
  snippets = Snippet.objects.all().order_by('-created_at')
  return render(request, 'codegiggles_app/snippets.html', {'snippets': snippets})

def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the snippets page after successful submission
            return redirect('snippets')  
    else:
        form = SnippetForm()

    return render(request, 'codegiggles_app/add_snippet.html', {'form': form})

def snippet_detail(request, snippet_id):
   snippet = get_object_or_404(Snippet, pk=snippet_id)
   return render(request, 'codegiggles_app/snippet_detail.html', {'snippet': snippet})

def like(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    snippet.likes += 1
    snippet.save()
    return HttpResponseRedirect(reverse('snippets'))

def dislike(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    snippet.dislikes += 1
    snippet.save()
    return HttpResponseRedirect(reverse('snippets'))

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