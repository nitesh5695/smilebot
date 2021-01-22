from django.shortcuts import render
from .models import user_profile,post_model
import io
from .serializer import profile_serializer,post_serializer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def user_profiles(request):
   if request.method=='GET':
        try:
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            username=pythondata.get('user_name',None)
            password=pythondata.get('password',None)
        except: 
            res={'error':'please provide your mail and password'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')    
      
        if username and password:
            get_profile=user_profile.objects.all().filter(user_name=username,password=password)
            serializer=profile_serializer(get_profile,many=True)
            json_data=JSONRenderer().render(serializer.data)
            print(len(serializer.data))
            if len(serializer.data)==0:
                 res={'error':'invalid_username or password'}
                 json_data=JSONRenderer().render(res)
                 return HttpResponse(json_data,content_type='application/json')   
            
            else:
                 return HttpResponse(json_data,content_type='application/json')   
        else:
              pass
         
@csrf_exempt
def upload_post(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=post_serializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'mesaage':'post created successfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json') 
        else:
            return HttpResponse(JSONRenderer().render({'error':'data is not valid'}),content_type='application/json')
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('title')
        post=post_model.objects.get(title=title)
        post.delete()
        res={'mesaage':'post successfully deleted'}
        return HttpResponse(JSONRenderer().render(res),content_type='application/json')

    if request.method=='GET':

         res={'mesaage':'this endpoint is only used to post data','fields':'title,description'}
         return HttpResponse(JSONRenderer().render(res),content_type='application/json')
def see_posts(request):
     if request.method=="GET":
        print("get")
        get_posts=post_model.objects.all()
        serializer=post_serializer(get_posts,many=True)
        json_data=JSONRenderer().render(serializer.data)
        print(len(serializer.data))
        if len(serializer.data)==0:
                res={'error':'no post found'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')  
        else:
             return HttpResponse(json_data,content_type='application/json') 






                


