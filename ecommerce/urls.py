from django.urls import path
from .views import signup,homepage,signin,user_logout,changepassword,editprofile,product,addproduct

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
]