from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def rohit(request):
    return HttpResponse('<h1>rohit is caption of mumbai indian team</h1>')
