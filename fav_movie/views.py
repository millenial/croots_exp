# Create your views here.
from django.template import Context, Template
from django.shortcuts import render
from django.http import HttpResponse

def listmovies(request):
    t = Template('hello world')
    return HttpResponse('hello world')

