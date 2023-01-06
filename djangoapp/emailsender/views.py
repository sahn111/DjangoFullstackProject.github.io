from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class SendEmail(forms.Form):
    email = forms.EmailField(label = "Email Address")

#continue and complete email operations

def index(request):
    subject = 'welcome to GFG world'
    message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("hello world")