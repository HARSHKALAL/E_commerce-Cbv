from django.shortcuts import render,redirect
from .forms import Userform,EditProfileForm,AddProductForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from .models import User,Category,Product

def homepage(request):  
    category_name = request.GET.get('cat')    
    categories=Category.objects.filter(is_deleted=False) 
    if category_name:
        categories=categories.filter(name__icontains=category_name)
    return render(request,"enroll/homepage.html",{'categories':categories})

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

def product(request,id):
    product=Product.objects.get(id=id)
    print(product.name)
    return render(request,'enroll/product.html',{'product':product})
    
def addproduct(request):      
    # if request.method == 'POST':
    #     add_product_form=AddProductForm(request.POST,request.FILES)
    #     if add_product_form.is_valid():
    #         add_product_form.save()
    #         return HttpResponseRedirect("/homepage/")
    #     else:
    #         print(add_product_form.errors)
    # else:
    if request.method == 'POST':
        print(request.POST)
        p_name=request.POST['p_name']
        p_text=request.POST['p_text']
        p_description=request.POST['p_description']
        p_image=request.POST['p_image']
        p_sold_by=request.POST['p_sold_by']
        p_price=request.POST['p_price']
        p_discount_percentage=request.POST['p_discount_percentage']
        p_category=request.POST['p_category']
        p_stock_quantity=request.POST['p_stock_quantity']


        pro=Product.objects.create(name=p_name,text=p_text,description=p_description,image=p_image,price=p_price,discount_percentage=p_discount_percentage,stock_quantity=p_stock_quantity)
        pro.category.add(p_category)
        pro.save()
        pro.sold_by.add(p_sold_by)
        pro.save()
        return HttpResponseRedirect('/homepage/')
        # pro=Product(name=p_name,tex=p_text,description=p_description,image=p_image,sold_by=p_sold_by,price=p_price,discount_percentage=p_discount_percentage,category=p_category,stock_quantity=p_stock_quantity)

    add_product_form=AddProductForm()
    return render(request,"enroll/addproduct.html",{'add_product_form':add_product_form})

