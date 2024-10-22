from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("<int:pk>/", views.detail, name="detail"),
    path("/new/", views.create, name="create"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/delete/", views.delete, name="delete")
]
