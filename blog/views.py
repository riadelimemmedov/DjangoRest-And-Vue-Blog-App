from django.shortcuts import render,get_object_or_404,HttpResponse
from rest_framework import generics,views,response,status,permissions
from .permissions import *
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *
from user_profile.models import *
from user_profile.serializers import *

# Create your views here.

#!BlogListCreateView
@method_decorator(csrf_exempt,name='dispatch')
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer

    def perform_create(self,serializer):
            if self.request.method == 'POST':
                print(self.request.POST)
                print('Vue terefden axiosdan POST request geldi yoxlama ucun')
                print('Method Value ', self.request.method)
                return HttpResponse('Ugurlu bir post reqeust vue terefinden hemde cookie')
                #profile = Profile.objects.get(user=self.request.user)
                #serializer.save(owner=profile)

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
        serializer.save(owner=profile)

#!CommentBlogDetail
class CommentBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentBlog.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

