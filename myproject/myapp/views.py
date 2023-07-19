from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import DictionaryEntry
from .forms import AddWordForm


# Create your views here.
def hello(request):
    return HttpResponse("Hello, Naija")


def page_view(request):
    return render(request, 'naija_dict/page.html')


def search_view(request):
    query = request.GET.get('query')
    results = DictionaryEntry.objects.filter(word__icontains=query)
    context = {'results': results}
    return render(request, 'naija_dict/page.html', context)

def add_word_view(request):
    form = AddWordForm()

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('init')
    else:
        form = AddWordForm()

    context = {'add_word_form': form}
    return render(request, 'naija_dict/page.html', context)
