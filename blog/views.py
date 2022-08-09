import django
from django.shortcuts import render,get_object_or_404,HttpResponse
from requests import Response
from rest_framework import generics,views,response,status,permissions,viewsets
from rest_framework.response import Response
from .permissions import *
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

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
                header_token = self.request.META.get('HTTP_AUTHORIZATION', None)
                print('Header Token ', header_token)
                print('Vue terefden axiosdan POST request geldi yoxlama ucun')
                print('Method Value ', self.request.method)
                return HttpResponse('Ugurlu bir post reqeust vue terefinden hemde cookie')
                #profile = Profile.objects.get(user=self.request.user)
                #serializer.save(owner=profile)
                
#!BlogDetailView
class BlogDetailView(views.APIView):
    def get_object(self,pk=None):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            print('Err')

    def get(self,request,pk,format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog,context={'current_user':request.user})
        return Response(serializer.data)
        
#!CategoryListCreateView

class CategoryBlogListCreateView(generics.ListCreateAPIView):
    queryset = CategoryBlog.objects.all()
    serializer_class = CategoryBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(owner=profile)

#!CommentBlogListCreateView
@method_decorator(csrf_exempt,name='dispatch')

class CommentBlogListCreateView(generics.ListCreateAPIView):
    queryset = CommentBlog.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        # user_fuck = Token.objects.get(key=self.request.POST['user_token'])
        # print('blet', user_fuck)
        if self.request.method == 'POST':
            print('Axios Comment Data ', self.request.POST)
            profile = Profile.objects.get(user=self.request.user)
            serializer.save(owner=profile)

#!CommentBlogDetail
class CommentBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentBlog.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]#IsOwnerOrReadOnly


#!get_csrf_token
def get_csrf_token(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'token': token})

