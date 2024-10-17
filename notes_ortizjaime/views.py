from django.shortcuts import render

# Create your views here.
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
