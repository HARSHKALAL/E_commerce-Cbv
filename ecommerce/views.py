from django.shortcuts import render,redirect
from .forms import Userform,EditProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import User,Category,Product,MerchantFirm,Carousel,Cart,Order
import json
from django.db.models import Sum,F,DecimalField,ExpressionWrapper,Value
from .utils import *
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict


def homepage(request):  
    category_name = request.GET.get('cat')    
    categories=Category.objects.filter(is_deleted=False) 
    carousel_image=Carousel.objects.order_by('image')[0:3]
    cart_count=Cart.objects.filter(user_id=request.user.id).aggregate(Sum('quantity'))
    
    if category_name:
        categories=categories.filter(name__icontains=category_name)
    return render(request,"enroll/homepage.html",{'categories':categories,"carousel_image":carousel_image,"cart_count":cart_count})

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
    return render(request,'enroll/product.html',{'product':product})
    
def addproduct(request): 
    solds_by=MerchantFirm.objects.all()
    category=Category.objects.all()

    if request.method == 'POST':
        p_name=request.POST['name']
        p_text=request.POST['text']
        p_description=request.POST['description']
        p_image=request.FILES['image']
        p_sold_by=request.POST['sold_by']
        p_price=request.POST['price']
        p_discount_percentage=request.POST['discount_percentage']
        p_category=request.POST['category']
        p_stock_quantity=request.POST['stock_quantity']

        pro=Product.objects.create(name=p_name,text=p_text,description=p_description,image=p_image,price=p_price,discount_percentage=p_discount_percentage,stock_quantity=p_stock_quantity)
        pro.category.add(p_category)
        pro.save()
        pro.sold_by.add(p_sold_by)
        pro.save()  
        return HttpResponse("created")

    return render(request,"enroll/addproduct.html",{'solds_by':solds_by,'category':category})

def update_product(request,id):
    solds_by=MerchantFirm.objects.all()
    category=Category.objects.all()    
    product=Product.objects.get(id=id)

    print(product.category.all().values_list('id'))

    if request.method == 'POST':
        print(request.POST)
        p_name=request.POST['name']
        p_text=request.POST['text']
        p_description=request.POST['description']
        p_image=request.FILES['image']
        sold_by_old=request.POST['sold_by']
        p_price=request.POST['price']
        p_discount_percentage=request.POST['discount_percentage']
        cat_old=request.POST['category_list']
        print(cat_old)
        p_stock_quantity=request.POST['stock_quantity']


        cat_updated = json.loads(cat_old)
        sold_by_updated = json.loads(sold_by_old)

        print(cat_updated)

        pro=Product.objects.filter(id=id)
        
        pro.update(name=p_name,text=p_text,description=p_description,price=p_price,discount_percentage=p_discount_percentage,stock_quantity=p_stock_quantity)
        pro=pro.first()
        
        if p_image:
            pro.image=p_image
            pro.save()

        if cat_updated:
            pro.category.set(cat_updated)
            pro.save()
        
        if sold_by_updated:
            pro.sold_by.set(sold_by_updated)
            pro.save()

    print("Data Received")    
    return render(request,"enroll/update_product.html",{'solds_by':solds_by,'category':category,'product':product})

def delete_product(request,id):
    delete_product=Product.objects.get(id=id).delete()
    return HttpResponseRedirect("/homepage/")

def remove_category(request,id,p_id):
    product=Product.objects.get(id=p_id)
    product.category.remove(id)    
    return HttpResponse("Deleted")

def remove_sold_by(request,id,p_id):
    product=Product.objects.get(id=p_id)
    product.sold_by.remove(id)    
    return HttpResponse("Deleted")


def cart_product(request,id):
    print(id)
    print(request.user.id)
    cart=Cart.objects.get_or_create(user_id=request.user.id,product_id=id)
    return HttpResponse("Created Successfully")

def view_cart(request):
    cart_view=Cart.objects.filter(user=request.user.id)

    cart_total_final = Cart.objects.filter(user_id=request.user.id).annotate(sum_total = ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField()))
    final_show = cart_total_final.values("sum_total").annotate(totals=Sum("sum_total"))
    new_try = final_show.aggregate(total=Sum('totals'))
      
    return render(request,"enroll/cart.html",{'cart_view':cart_view,"total":new_try.get('total')})

def remove_cart_Product(request,id):
    cart_product=Cart.objects.get(id=id).delete()    
    return HttpResponse("Delete")

def update_cart_Product(request,id):
    if request.method == 'POST':
        add=request.POST['add']

        cart_total_final = Cart.objects.filter(user_id=request.user.id).annotate(sum_total = ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField()))
        final_show = cart_total_final.values("sum_total").annotate(totals=Sum("sum_total"))
        new_try = final_show.aggregate(total=Sum('totals'))        
        
        cart_product=Cart.objects.get(product_id=id,user_id = request.user.id)                      
        if  cart_product.product.stock_quantity <= cart_product.quantity :                        
            return HttpResponse("not available")
        else:
            if add == 'add':
                cart_product.quantity = cart_product.quantity + 1    
                cart_product.save()
                return JsonResponse({"msg":"added in cart","qty":cart_product.quantity,"price":cart_product.product.price,"total":new_try.get('total')})
            else:
                if cart_product.quantity == 1:
                    cart_product.delete()
                    return JsonResponse({"msg":"not in stock","price":cart_product.product.price,"total":new_try.get('total')})
                else:
 
                    cart_product.quantity = cart_product.quantity - 1    
                    cart_product.save()
                    return JsonResponse({"msg":"removed from cart","qty":cart_product.quantity,"price":cart_product.product.price,"total":new_try.get('total')})

def confirm_order(request):
    total=request.POST['totalamount']
    total_updated = json.loads(total)
        
    order_confirmation=Cart.objects.filter(user_id=request.user.id)
    order_data=order_confirmation.values('product_id','product__price','product__stock_quantity','quantity')

    data_json = json.loads(json.dumps(list(order_data, cls=DecimalEncoder)))

    orders=[]
    for order in  order_confirmation:
        data={"product_id":order.product.id,"price":str(order.product.price),"quantity":order.quantity}
        orders.append({"data":data,"stock_quntity":order.product.stock_quantity})
    
    order_confirm=Order.objects.create(user_id=request.user.id,total_amount=total_updated,order_details=data_json)
    total_stock_quantity(order_data)
    return render(request,"enroll/confirm_order.html")

def my_orders(request):
    my_order=Order.objects.filter(user_id=request.user.id)
    order_data=list(my_order.values('order_details'))
    return render(request,"enroll/my_orders.html",{'my_order':my_order,"product_details":order_json_to_products(order_data)})



