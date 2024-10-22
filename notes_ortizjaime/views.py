from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import User, Note 
from django.db.models import F
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from . forms import CreateUserForm, LoginForm, NoteForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def index(request):
    # user = User.objects.create_user(username='john',email='jlennon@beatles.com',password='glass onion')
    notes_list = Note.objects.order_by("-creation_date" )
    context = {"notes_list" : notes_list}
    return render(request,"note/note_index_ortiz_jaime.html",context)

@login_required(login_url="/notes/login")
def list(request):
    notes = Note.objects.filter(user=request.user)
    context = {"notes_list" : notes}
    return render(request,"note/note_list_ortiz_jaime.html", context)

def detail(request,pk):
    note = get_object_or_404(Note,pk = pk)
    return render(request,"note/note_detail_ortiz_jaime.html",{"note":note})

def create(request): 
    form = NoteForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect("/notes/list")
    else:
        form = NoteForm()
    return render(request,"note/note_create_ortiz_jaime.html",{"noteform" : form})

def edit(request,pk):
    note = get_object_or_404(Note,pk = pk)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/notes/list")
    else:
        form = NoteForm()
    return render(request,"note/note_edit_ortiz_jaime.html",{"noteform" : form})

def delete(request,pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return HttpResponseRedirect(reverse('notes:list'))
    return HttpResponse("Delete a note") 

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect("/notes/list")
    return render(request,"note/note_login_ortiz_jaime.html",{"loginform":form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/notes/")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/notes/login/") 
    return render(request,"note/note_register_ortiz_jaime.html",{"registerform" : form})
