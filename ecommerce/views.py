from django.shortcuts import render,redirect
from .forms import Userform,EditProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from .models import User,Category

def homepage(request):    
    category_list=Category.objects.all()
    return render(request,"enroll/homepage.html",{'category_list':category_list})

def signup(request):
    form=Userform()
    if request.method == "POST":
        form=Userform(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            print(form)
            form.save()  
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

def user_logout(request):
    print(request)
    logout(request)
    return HttpResponseRedirect('/signin/')

def changepassword(request):
    if request.method == "POST":
        change_pass=PasswordChangeForm(data=request.POST,user=request.user)
        if change_pass.is_valid():
            change_pass.save()
            return HttpResponseRedirect('/homepage/')
    else:
        change_pass=PasswordChangeForm(user=request.user)
    return render(request,'enroll/changepassword.html',{'change_pass':change_pass})

def editprofile(request):
    if request.method == 'POST':
        edit_form=EditProfileForm(request.POST,request.FILES,instance=request.user)
        print("edit")
        if edit_form.is_valid():  
            print("edit")
            edit_form.save()  
            print("Update success")
            return HttpResponseRedirect("/homepage/")  
        else:
            print(edit_form.errors)
    else:
        edit_form=EditProfileForm(instance=request.user)
    return render(request,'enroll/editprofile.html',{'edit_form':edit_form})

