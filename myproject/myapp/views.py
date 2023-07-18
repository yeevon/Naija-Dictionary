from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello, Naija")


def page_view(request):
    return render(request, 'naija_dict/page.html')
