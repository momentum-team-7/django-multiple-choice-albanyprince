from django.shortcuts import render
from .models import Snippet
# Create your views here.

def snippet_post(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/index.html', {'snippets': snippets})

        