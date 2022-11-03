from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","logo"]        
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','id':"usernameid",'required':"False"}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':"emailid"}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','id':"password1id"}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','id':"password2id"}),
            'logo':forms.FileInput(attrs={'class':'form-control','id':"logoid"}),
        }



