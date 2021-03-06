from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance='snippet')
        if form.is_valid()
        return HttpResponseRedirect('')

    else:
        snippet = SnippetForm(instance='snippet')
    return render(request, 'core/edit_snippet.html', {'form':form, 'snippet':snippet})