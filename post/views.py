from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, I am from post app")

def show(request, slug):
	return HttpResponse("You're looking at post %s." % slug)