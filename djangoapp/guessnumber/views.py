from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.conf import settings
import random
import datetime
from djangoapp.forms.SendEmailForm import SendEmail

class GuessNumber(forms.Form):
    number = forms.IntegerField(label = "Make Guess", min_value = 1, max_value =5)

def guess(request):
    if "number" not in request.session and "true" not in request.session and "false" not in request.session:
        request.session["number"] = []
        request.session["true"] = []
        request.session["false"] = []

    if request.method == "POST":
        form = GuessNumber(request.POST)
        if form.is_valid():
            num =   form.cleaned_data['number']
            request.session["number"] += [num]
            rand_num = random.randint(0,5)
            print(f"Result is {rand_num}")
            if num==rand_num:
                request.session["true"] += [num]
            else:
                request.session["false"] += [num]

            return render(request, "guessnumber/index.html",{
                "rand_num":rand_num,
                "number": num==rand_num,
                "form" : GuessNumber() 
            })
        else:
            return render(request, "guessnumber/index.html",{
                "number": False,
                "form" : GuessNumber() 
            })

    else:
        return render(request, "guessnumber/index.html",{
            "number": True,
            "form" : GuessNumber() 
        })

def showguess(request):

    if request.session["true"] != [] and request.session["false"] != []:
        rate = len(request.session["true"])/(len(request.session["true"])+len(request.session["false"]))
    elif request.session["true"] != [] and request.session["false"] == []:
        rate = 100
    else:
        rate = 0

    return render(request, "guessnumber/showguess.html",{
        "form": SendEmail(initial={'rate':rate}),
        "true_list" : request.session["true"],
        "false_list" : request.session["false"], 
        "number": request.session["number"],
        "rate": rate,
    })
    
def delete(request):

    request.session["number"] = []
    request.session["true"] = []
    request.session["false"] = []

    return HttpResponseRedirect(reverse("guessnumber:index"))

def add(request):
    return render(request, "guessnumber/add.html")