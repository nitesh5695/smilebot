from django.contrib import admin
from .models import user_profile,post_model

@admin.register(user_profile)
class  user(admin.ModelAdmin):
    display_list=['id','user_name','password','name','gender','age']


@admin.register(post_model)
class  posts(admin.ModelAdmin):
    display_list=['description','title','likes','publish_date']    