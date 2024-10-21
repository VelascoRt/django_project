from django.urls import path
from . import views

app_name = "project_ortizjaime"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("detail/", views.detail,name="detail"),
    path("create/", views.create,name="create"),
    path("edit/", views.edit,name="edit"),
    path("delete/", views.delete,name="delete")
]
