from django.shortcuts import render
from .models import Snippet

def home(request):
  #! latest 8 snippets
  snippets = Snippet.objects.all()[:8]
  return render(request, 'codegiggles_app/home.html', {'snippets': snippets})
 
def snippets(request):
  snippets = Snippet.objects.all()
  return render(request, 'codegiggles_app/snippets.html', {'snippets': snippets})