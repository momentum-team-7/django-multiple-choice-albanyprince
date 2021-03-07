from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from .models import User
from .models import Snippet
from .forms import SnippetForm
# Create your views here.

@login_required
def index(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/index.html', {'snippets': snippets})

@login_required
def developer_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'core/developer_profile.html', {'user':user})

def add_snippet(request):
    if request.method =='POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return HttpResponseRedirect('/')
    else:
        form = SnippetForm()
    return render(request, 'core/add_snippet.html', {'form': form})            

@login_required
def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'core/edit_snippet.html', {'form':form, 'snippet':snippet})


def copy_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'core/copy_snippet.html', {'form':form, 'snippet':snippet})


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return HttpResponseRedirect('/')