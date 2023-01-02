from django.urls import path
from .views import Signup,Homepage,LogoutView,editprofile,product,addproduct,update_product,remove_category,remove_sold_by,delete_product,cart_product,view_cart,remove_cart_Product,update_cart_Product,confirm_order,my_orders
from django.contrib.auth import views as auth_views
urlpatterns =[     
    path('homepage/', Homepage.as_view(), name='homepage'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/',LogoutView.as_view(),name="logout"),    



    path('editprofile/',editprofile,name="editprofile"),    
    path('product/<int:id>/',product,name="product"),
    path('addproduct/',addproduct,name="addproduct"),   
    path('update_product/<int:id>/',update_product,name="update_product"),
    path('delete_product/<int:id>/',delete_product,name="delete_product"),
    path('remove_category/<int:id>/<int:p_id>/',remove_category,name="remove_category"),
    path('remove_sold_by/<int:id>/<int:p_id>/',remove_sold_by,name="remove_sold_by"),
    path('cart_product/<int:id>/',cart_product,name="cart_product"),
    path('view_cart/',view_cart,name="view_cart"),
    path('remove_cart_Product/<int:id>/',remove_cart_Product,name="remove_cart_Product"),
    path('update_cart_Product/<int:id>/',update_cart_Product,name="update_cart_Product"),
    path('confirm_order/',confirm_order,name="confirm_order"),
    path('my_orders/',my_orders,name="my_orders"),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='enroll/changepassword.html',
            success_url = '/homepage/'
        ),
        name='change_password'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='enroll/login.html',
            success_url = '/homepage/'
        ),
        name='login'
    ),
    
]