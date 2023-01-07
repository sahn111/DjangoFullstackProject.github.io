from django.urls import path

from . import views

app_name = "emailsender"
urlpatterns = [
    path("", views.index, name="index")
]