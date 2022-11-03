from django.shortcuts import render
from .forms import Userform

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
    pass
