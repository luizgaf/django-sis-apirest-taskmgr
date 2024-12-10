from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as djangologin
from django.contrib.auth.decorators import login_required

def mainpage(request):
    if request.method == "GET":
        return render(request, 'mainpage.html')

@login_required(login_url="/auth/login/")
def portal(request):
    return render(request, 'portal.html')
