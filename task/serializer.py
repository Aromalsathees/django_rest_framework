from rest_framework import serializers  
from .models import Task


# This is MODEL SERIALIZER .
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task 
#         fields = '__all__'



# This is Basic serializer
class TaskSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)
    desc = serializers.CharField(max_length=100)

    # Data create operation using BASIC SERIALIZER
    def create(self, validated_data):
        return Task.objects.create(
            **validated_data
        )
    
    # Data update operation using BASIC SERIALIZER
    def update(self, instance, validated_data):
        
        instance.name = validated_data.get("name",instance.name)
        instance.desc = validated_data.get("desc",instance.desc)

        instance.save()
        return instance
