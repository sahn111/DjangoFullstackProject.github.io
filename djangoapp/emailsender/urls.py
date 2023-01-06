from django.urls import path
from django.conf import settings

from . import views

app_name = "emailsender"
urlpatterns = [
    path("", views.index, name="index")
]