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
    return render(request,"note/note_index_ortiz_jaime.html",context)

def list(request):
    notes = Note.objects.all()
    context = {"notes_list" : notes}
    return render(request,"note/note_list_ortiz_jaime.html", context)

def detail(request,pk):
    note = get_object_or_404(Note,pk = pk)
    return render(request,"note/note_detail_ortiz_jaime.html",{"note":note})

def create(request):
    return HttpResponse("create notes")

def edit(request):
    return HttpResponse("edit a notes")

def delete(request):
    return HttpResponse("Delete a note")
