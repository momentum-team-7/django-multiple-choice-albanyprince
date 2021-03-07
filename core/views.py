from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from .models import User, Snippet
from .forms import SnippetForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.

@login_required
def index(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/index.html', {'snippets': snippets})

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


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance='snippet')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        snippet = SnippetForm(instance='snippet')
    return render(request, 'core/edit_snippet.html', {'form':form, 'snippet':snippet})


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return HttpResponseRedirect('')

# class HomePageView(TemplateView):
#     template_name = 'home.html'


class SearchResultsView(ListView):
    model = Snippet
    template_name = 'core/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        snippet_list = Snippet.objects.filter(Q(code__icontains=query) | Q(language__icontains=query) |Q(title__icontains=query))
        
        return snippet_list
# def results(request, pk):
#     search_input = request.GET['query']
#     results = Sinppet.obejcts.filter()        