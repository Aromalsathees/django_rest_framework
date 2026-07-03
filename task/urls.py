from django.urls import path  
from .views import *

urlpatterns = [
    path('',home.as_view()),
    path('delete_student/<int:get_id>/',remove_student.as_view()),
    path('alter_student/<int:id>/',update_student.as_view()),
]

