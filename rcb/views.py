from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def virat(request):
    return HttpResponse('<h1>virat kholi is caption of Royal Challengers Bengaluru team</h1>')