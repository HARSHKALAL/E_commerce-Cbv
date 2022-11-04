from django.urls import path
from .views import signup,homepage,signin


urlpatterns =[     
    path('homepage/',homepage,name="homepage"),
    path('signup/',signup,name='register'),
    path('signin/',signin,name="signin"),
]