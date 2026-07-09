from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializer import SignupSerializer
# Create your views here.


class Signup(APIView):
    
    permission_classes = [AllowAny]
    def post(self, request):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            token = Token.objects.create(user=user)

            return Response({
                'message':'successfully registed your account',
                'token':token.key
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message':'faileddd',
            'error':serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    


class Login(APIView):
    
    permission_classes = [AllowAny]
    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
            )

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response(
                    {
                    'message':'Login successfull',
                    'token':token.key
                    })
            
        return Response({
                'message':'invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class home(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            'username':request.user.username
        })