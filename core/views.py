from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from .models import User, Snippet
# Create your views here.

@login_required
def index(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/index.html', {'snippets': snippets})

def developer_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'core/developer_profile.html', {'user':user})
