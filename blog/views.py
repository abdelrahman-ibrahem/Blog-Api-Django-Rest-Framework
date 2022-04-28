# blog/views.py
from django.shortcuts import render
from .models import Post
from .serializers import PostApi 
from rest_framework import generics , permissions , viewsets
from .permissions import IsAutherOrReadOnly

# class PostListView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostApi


# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAutherOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostApi


# use viewsets for reducing the repeating code 
# class for posts
class PostView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , IsAutherOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostApi
