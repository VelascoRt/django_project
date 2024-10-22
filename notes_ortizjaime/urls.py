from django.urls import path
from . import views

app_name = "project_ortizjaime"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("<int:pk>/", views.detail,name="detail"),
    path("<int:pk>/create/", views.create,name="create"),
    path("<int:pk>/edit/", views.edit,name="edit"),
    path("<int:pk>/delete/", views.delete,name="delete")
]
