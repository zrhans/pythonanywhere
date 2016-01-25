from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django import forms


# Create your views here.
def home(request):
    """docstring for home"""
    return render(request,"home.html",{})

def hello(request):
    name = "Hans"
    html = "<html><body>Oi %s, parece que funciona!" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Hans"
    return render(request,"hello.html",{'name':name})

# Metodos para as urls de user login
#===================================
def login(request):
    c = {}
    c.update(csrf(request))
    #return render(request, 'login/login.html',c)
    return render(request,'login/login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin/')#render(request,'login/loggedin.html',{'full_name':request.user.username})
    else:
        return render(request,'login/invalid-login.html')

def loggedin(request):
    return render(request,'login/loggedin.html',{'full_name':request.user.username})

def invalid_login(request):
    return render(request,'login/invalid-login.html')

def logout(request):
    auth.logout(request)
    #return HttpResponse('logout.html')
    return HttpResponseRedirect('/uterg/')#render(request,'bns/home.html')
