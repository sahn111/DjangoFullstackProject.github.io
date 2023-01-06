from django.urls import path

from . import views

app_name = "guessnumber"
urlpatterns = [
    path("", views.guess, name="index"),
    path("showguess", views.showguess, name="showguess"),
    path("add", views.add, name="add")
]