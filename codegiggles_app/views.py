from django.shortcuts import render, redirect
from .models import Snippet
from .forms import SnippetForm

def home(request):
  #! latest 8 snippets
  snippets = Snippet.objects.all()[:8]
  return render(request, 'codegiggles_app/home.html', {'snippets': snippets})
 
def snippets(request):
  snippets = Snippet.objects.all()
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