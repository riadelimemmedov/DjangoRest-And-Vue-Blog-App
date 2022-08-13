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
class BlogListCreateView(views.APIView):
    def get(self,request):
        blogs = Blog.objects.all().order_by('-created')
        serializer = BlogSerializer(blogs,many=True)
        
        current_user = ''
        usertoken = self.request.GET['user_token']
        if usertoken:
            current_user = Token.objects.get(key=usertoken).user
            profile_serializer = UserSerilizers(current_user)
            print(' User Serializer ', profile_serializer.data)
            print('IF isledi ve blog ve userlar geri dondu response ile')
            return Response({'serializer_data':serializer.data,'current_user':profile_serializer.data},status=status.HTTP_200_OK)
        else:
            print('Ancag postlar geri dondu cunki user giris etmeyib')
            return Response({'serializer_data':serializer.data},status=status.HTTP_200_OK)


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
        user = Token.objects.get(key='1d6b91bee50efa3f158f3f6b4d0ab218f26ab089').user
        comments = CommentBlog.objects.filter(blog_id=pk)
        print('Comment lIST HER BLOG ', comments)
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        commentserializer = CommentSerializer(comments,many=True)
        print(commentserializer)
        print('Serialize commenrt serializer ' , commentserializer.data)
        return Response({'serializer':serializer.data,'commentserialize':commentserializer.data})
        
#!CategoryListCreateView

class CategoryBlogListCreateView(generics.ListCreateAPIView):
    queryset = CategoryBlog.objects.all()
    serializer_class = CategoryBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        print('Comment' , self.request.POST)
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(owner=profile)

#!CommentBlogListCreateView

class CommentBlogListCreateView(generics.ListCreateAPIView):
    queryset = CommentBlog.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        # user_fuck = Token.objects.get(key=self.request.POST['user_token'])
        # print('blet', user_fuck)
        print('Fuck isledi perform create commentde')
        print(self.request.POST)
        
        if self.request.method == 'POST':
            user = Token.objects.get(key=self.request.POST.get('token')).user
            print('User ', user)
            print('Axios Comment Data ', self.request.POST)
            profile = Profile.objects.get(user=user)
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

