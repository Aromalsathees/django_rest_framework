from django.urls import path  
from .views import *  



urlpatterns = [
    path('',home.as_view()),
    path('api/signup/', Signup.as_view()),
]