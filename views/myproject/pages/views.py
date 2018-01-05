from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def HomePageView(request):
    return HttpResponse('<h1>Hello World..!!</h1>')
