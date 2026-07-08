from django.urls import path  
from .views import *  

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('home/',home.as_view()),
    path('signup/', Register_view.as_view()),
    path('logout/', Logout.as_view()),

    path('login/',TokenObtainPairView.as_view()),

    path('refresh/',TokenRefreshView.as_view()),

    
]