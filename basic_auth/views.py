from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response  
from rest_framework import status 
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import SignupSerializer
# Create your views here.


class Signup(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'user registed successfull'
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message':'field error',
            'errors':serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class home(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message':'welcome to home page',
            'username':request.user.username
        })


# request.POST.get('name')
# request.POST['get']


# request.data.get
# request.data
# request.body