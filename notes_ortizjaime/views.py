from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect 

# Create your views here.

def index(request):
    return HttpResponse("This is the index")

def list(request):
    return HttpResponse("This is where the notes are gonna be")

def detail(request):
    return HttpResponse("Detail of notes")

def create(request):
    return HttpResponse("create notes")

def edit(request):
    return HttpResponse("edit a notes")

def delete(request):
    return HttpResponse("Delete a note")
