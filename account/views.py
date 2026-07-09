from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializer import RegistserSerializer

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class Register_view(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):

        serializer = RegistserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'message':'successfully registerd user',
                'data':serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
                'message':'fill all fields correctly',
                'data':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

class Logout(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):

        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({
                'message':'Logged out successfully'
            })
        
        except Exception as e:

            return Response({
                'error': str(e)
            })


class home(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        return Response({
            'message': request.user.username
        })
    


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MzY0ODU5MywiaWF0IjoxNzgzNTYyMTkzLCJqdGkiOiI2YjczNmE0MzBmYTE0OTRkOTJlNmJmM2Y0YWE2N2NjMiIsInVzZXJfaWQiOiI5In0.AiLvdIVr-q1CQjU6GCtJHgcpYJ7rcLJQIaORbTnk_gI",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgzNTYyNDkzLCJpYXQiOjE3ODM1NjIxOTMsImp0aSI6Ijk2NmQxNzEyNTdiZTRhYWE4NWEwNzJhOWM4ZDA0OGU2IiwidXNlcl9pZCI6IjkifQ.20mt_cJMHUp-LVwsA3YSyuJ3zx6wEvNNXkTozYdp3vA"
# }