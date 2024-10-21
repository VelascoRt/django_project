from django.urls import path
from . import views

app_name = "project_ortizjaime"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("<int:note_id>/", views.detail,name="detail"),
    path("<int:note_id>/create/", views.create,name="create"),
    path("<int:note_id>/edit/", views.edit,name="edit"),
    path("<int:note_id>/delete/", views.delete,name="delete")
]
