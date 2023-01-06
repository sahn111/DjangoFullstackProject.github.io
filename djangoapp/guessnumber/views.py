from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime
# Create your views here.

def guess(request, number):
    num = random.randint(0,5)
    print(f"Result is {num}")

    return render(request, "guessnumber/index.html",{
        "number": number==num
    })
    