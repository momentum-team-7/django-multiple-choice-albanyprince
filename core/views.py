from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from .models import User, Snippet
# Create your views here.

@login_required
def snippet_post(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/index.html', {'snippets': snippets})

        