from django.shortcuts import render
from .forms import Userform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from .models import User

def homepage(request):
        return render(request,"enroll/homepage.html")
def signup(request):
    form=Userform()
    if request.method == "POST":
        form=Userform(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            print(form)
            form.save()  
            print(form)  
            form=Userform()
    else:
        form=Userform()
    return render(request,"enroll/register.html",{'form':form})

def signin(request):
    loginform=AuthenticationForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/homepage/")
    else:
        loginform=AuthenticationForm()
    return render(request,'enroll/login.html',{'loginform':loginform})
