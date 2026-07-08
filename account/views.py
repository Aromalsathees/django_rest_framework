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
    


#     {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MzU2Nzk3MCwiaWF0IjoxNzgzNDgxNTcwLCJqdGkiOiI0NTkwMDI3ZDc1MWU0NjhkOTk2ZDI5NDBjMDk0YzU0MiIsInVzZXJfaWQiOiIzIn0.m1_-RbawGAVycA9ODqEugwroZUrH3iM15-_a9mznLX0",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgzNDgxODcwLCJpYXQiOjE3ODM0ODE1NzAsImp0aSI6IjVkYzkwMjFjYzFhMzQ5OTE4OGI5MTJiNDY4MmI4OTY2IiwidXNlcl9pZCI6IjMifQ.QpLZL_3rNp8HUinXMQF81-u9NWSdmB50UzuCkpItqbw"
# }