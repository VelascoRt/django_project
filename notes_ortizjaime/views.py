from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect 

# Create your views here.

def index(request):
    return HttpResponse("This is the index")

def list(request,note_id):
    note = get_object_or_404()
    return HttpResponse("This is where the notes are gonna be")

def detail(request):
    return HttpResponse("Detail of notes")

def create(request):
    return HttpResponse("create notes")

def edit(request):
    return HttpResponse("edit a notes")

def delete(request):
    return HttpResponse("Delete a note")
