from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import User

class Userform(UserCreationForm):
    class Meta:
        
        model = User
        fields = ["username", "email", "password1", "password2","logo"]        
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control my-1','id':"usernameid"}),
            'email':forms.EmailInput(attrs={'class':'form-control my-1','id':"emailid"}),
            'password1':forms.PasswordInput(attrs={'class':'form-control my-1','id':"password1id"}),
            'password2':forms.PasswordInput(attrs={'class':'form-control my-1','id':"password2id"}),
            'logo':forms.FileInput(attrs={'class':'form-control','id':"logoid"}),
        }