from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer
# Create your views here.


class home(APIView):

    def get(self,request):

        get_task = Task.objects.all()
        get_count = get_task.count()
        serializer = TaskSerializer(get_task,many=True)
        
        return Response({
            'message':'successfully got data',
            'data':serializer.data,
            'count':get_count
        },status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'successfully data created',
                'data':serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message':'all fileds are requried',
            'errors':serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class remove_student(APIView):

    def delete(self,request,get_id):

        try:
            student = Task.objects.get(id=get_id)
            student.delete()
            return Response({
                'message':f'The student {get_id} has deleted from Database'
            }, status=status.HTTP_200_OK)
        
        except Task.DoesNotExist:
            return Response({
                'message':f'The student {get_id} Does not exist on database'
            }, status=status.HTTP_404_NOT_FOUND)
        

class update_student(APIView):

    def put(self,request,id):

        try:
            get_student = Task.objects.get(id=id)
            serializer = TaskSerializer(instance=get_student, data=request.data)

            # get_student.name = request.POST.get('name')

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message':f'The student{id} has updated',
                    'data':serializer.data
                }, status=status.HTTP_200_OK)
            
            return Response({
                'message':'something happend with the input field',
                'error':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Task.DoesNotExist:
            return Response({
                'message':f'The id{id} does not exist on Database'
            }, status=status.HTTP_404_NOT_FOUND)





# def home(request,get_id):
#     try:
#         student = Task.objects.get(id=get_id)
#         student.delete()
#         message.success(request,'data deleted')
#         return redirect('home')
#     except Task.DoesNotExist:
#         messages.error('problem happend')
#         return redirect('home')



    

    # pip install django djangorestframework
    # rest_framework   resgitser it on the installed_apps