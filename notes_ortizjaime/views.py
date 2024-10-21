from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import User, Note 
from django.db.models import F
from django.urls import reverse
# Create your views here.

def index(request):
    notes_list = Note.objects.order_by("-creation_date" )
    context = {"notes_list" : notes_list}
    return render(render,"notes/index.html",context)

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
