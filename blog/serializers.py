from rest_framework import serializers 
from .models import Post
from django.contrib.auth import get_user_model

class PostApi(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('auther' , 'title' , 'body')
