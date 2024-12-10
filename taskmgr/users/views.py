from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as djangologin
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            djangologin(request, user)
            return plataforma(request)
        else:
            return HttpResponse('Nao foi possivel')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # validation:
        usernameExists = User.objects.filter(username=username).first()
        emailExisists = User.objects.filter(email=email).first()

        if usernameExists:
            return HttpResponse('Usuario existe')
        
        if emailExisists:
            return HttpResponse('Email ja cadastrado')
        
        else:
            user = User.objects.create_user(username, email, password)


        return HttpResponse(username)