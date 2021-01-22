from  rest_framework import serializers
from .models import post_model
from datetime import date
class profile_serializer(serializers.Serializer):
    user_name=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)
    name=serializers.CharField(max_length=100)
    gender=serializers.CharField(max_length=10)
    age=serializers.IntegerField()

class post_serializer(serializers.Serializer):
    description=serializers.CharField(max_length=255)
    title=serializers.CharField(max_length=200)
    likes=serializers.CharField(max_length=10,default=0)
    publish_date=serializers.DateField(default=date.today())
    def create(self,validated_data):
        return post_model.objects.create(**validated_data)