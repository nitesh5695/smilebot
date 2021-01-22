from django.db import models

class user_profile(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    def __str__(self) :
        return self.user_name

class post_model(models.Model):
   
    description=models.CharField(max_length=255)
    title=models.CharField(max_length=200)
    likes=models.CharField(max_length=10,default=1)
    publish_date=models.DateField()
    
           


     
