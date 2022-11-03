from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST,request.FILES)
        if form.is_valid():
            userName=request.POST['userName']
            userEmail=request.POST['userEmail']
            userPass1=request.POST['userPass1']            
            confirmPass=request.POST['confirmPass']
            userLogo=request.POST['userLogo']
            
            form.save()
            form = NewUserForm()
    return render(request,'enroll/register.html',{'form':form})
