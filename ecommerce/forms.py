from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from .models import User
class Userform(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center','placeholder':'Enter Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':' Enter Confirm password'}),
    )
    class Meta:
        model = User
        fields = ["username",'email','password1','password2']
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control my-1','id':"usernameid",'placeholder':'Enter UserName'}),
        'email':forms.EmailInput(attrs={'class':'form-control my-1','id':"emailid",'placeholder':'Enter Email'}),
        # 'logo':forms.FileInput(attrs={'class':'form-control','id':"logoid"}),      
        }  
class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=['username','email']
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control my-1','id':"usernameid",'placeholder':'Enter UserName'}),
        'email':forms.EmailInput(attrs={'class':'form-control my-1','id':"emailid",'placeholder':'Enter Email'}),
        }  