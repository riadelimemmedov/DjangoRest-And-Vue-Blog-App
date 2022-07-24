from django.shortcuts import render,get_object_or_404,HttpResponse
from rest_framework import generics,views,response,status,permissions
from .permissions import *
from django.core import serializers

from .models import *
from .serializers import *
from user_profile.models import *
from user_profile.serializers import *

# Create your views here.

#!BlogListCreateView
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(owner=profile)

#!CategoryListCreateView
class CategoryBlogListCreateView(generics.ListCreateAPIView):
    queryset = CategoryBlog.objects.all()
    serializer_class = CategoryBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(owner=profile)

#!CommentBlogListCreateView
class CommentBlogListCreateView(generics.ListCreateAPIView):
    queryset = CommentBlog.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=profile)

#!CommentBlogDetail
class CommentBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentBlog.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

