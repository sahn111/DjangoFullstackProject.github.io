from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from djangoapp.forms.SendEmailForm import SendEmail 

#continue and complete email operations

def index(request):
    if request.method == "POST":
        form = SendEmail(request.POST)
        if form.is_valid():
            print("here")
            user_email = form.cleaned_data["email"]#"9bc62cc6e55f3d@mailtrap.io"#
            subject = 'Welcome to GuessNumber'
            message = f'Hi, thank you for playing, your success rate is {form.cleaned_data["rate"]}.'
            email_from = settings.EMAIL_HOST_USER
            
            recipient_list = [user_email, ]
            print("send_mail working",user_email,subject,message,email_from)
            send_mail( subject, message, email_from, recipient_list, fail_silently=False )
    
    return HttpResponseRedirect(reverse("guessnumber:showguess"))
    