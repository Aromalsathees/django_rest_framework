from django.urls import path  
from .views import *

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', home)
urlpatterns = router.urls

# urlpatterns = [

#    

#     path('',home.as_view()),
#     # path('',home),


#     path('delete_student/<int:get_id>/',remove_student.as_view()),
#     path('alter_student/<int:id>/',update_student.as_view()),
#     path('get_one_student/<int:get_id>/',get_one_student.as_view()),
#     path('search/',search_data.as_view())
# ]





