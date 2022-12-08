from django.urls import path
from .views import signup,homepage,signin,user_logout,changepassword,editprofile,product,addproduct,update_product,remove_category,remove_sold_by,delete_product,cart_product,view_cart,remove_cart_Product,update_cart_Product

urlpatterns =[     
    path('',homepage,name="homepage"),
    path('homepage/',homepage,name="homepage"),
    path('signup/',signup,name='register'),
    path('signin/',signin,name="signin"),
    path('editprofile/',editprofile,name="editprofile"),    
    path('logout/',user_logout,name="logout"),
    path('changepassword/',changepassword,name="changepassword"),
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

]