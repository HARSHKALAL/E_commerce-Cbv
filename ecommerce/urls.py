from django.urls import path
from .views import signup,homepage


urlpatterns =[     
    path('',homepage,name="homepage"),
    path('signup/',signup,name='register'),
]