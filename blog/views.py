import django
from django.shortcuts import render,get_object_or_404
from requests import Response
from rest_framework import generics,views,response,status,permissions,viewsets
from rest_framework.response import Response
from .permissions import *
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from rest_framework.authtoken.models import Token
import json
from django.db.models import Q

from .models import *
from .serializers import *
from user_profile.models import *
from user_profile.serializers import *

# Create your views here.

#!BlogListCreateView
@method_decorator(csrf_exempt,name='dispatch')
class BlogListCreateView(views.APIView):
    def get(self,request,format=None):
        blogs = Blog.objects.all().order_by('-created')
        serializer = BlogSerializer(blogs,many=True)
        
        current_user = ''
        liked = None
        usertoken = self.request.GET.get('user_token')
        print('User Token Value ', usertoken)
        if usertoken:
            current_user = Token.objects.get(key=usertoken).user
            profile_serializer = UserSerilizers(current_user)
            
            # print(' User Serializer ', profile_serializer.data)
            # print('IF isledi ve blog ve userlar geri dondu response ile')
            return Response({'serializer_data':serializer.data,'current_user':profile_serializer.data},status=status.HTTP_200_OK)
        else:
            print('Ancag postlar geri dondu cunki user giris etmeyib')
            return Response({'serializer_data':serializer.data},status=status.HTTP_200_OK)


    def post(self,request,format=None):
            if self.request.method == 'POST' and self.request.POST.get('user_token') != '':
                #?Header Token Value
                header_token = self.request.META.get('HTTP_AUTHORIZATION', None)
                
                #?Liked Post Data For Liked Blog Post
                current_user = Token.objects.get(key=self.request.POST.get('user_token')).user
                liked_user = User.objects.get(username=current_user)
                print('Current User Model ', liked_user)
                blog_obj = Blog.objects.get(id=self.request.POST.get('blog_id'))
                blog_serializer = BlogSerializer(blog_obj)
                
                
                if current_user in blog_obj.liked.all():
                    print('Unlike Blog')
                    blog_obj.is_liked = False
                    #likes['is_user_liked'] = False
                    blog_obj.liked.remove(current_user)
                    blog_obj.save()
                else:
                    print('Like Blog')
                    blog_obj.is_liked = True
                    #likes['is_user_liked'] = True
                    blog_obj.liked.add(current_user)
                    blog_obj.save()
                    
                like,created = Like.objects.get_or_create(user=current_user,post=blog_obj)
                
                if not created:
                    print('Created Value ', created)
                    print('If created value when is true Like object not exists before crt')
                    if like.value == 'Like':
                        like.value = 'Unlike'
                        like.is_user_liked = True
                    else:
                        like.value = 'Like'
                        like.is_user_liked = False
                        
                print('Before save like value data ', like.value)
                like.save()
                return Response({'like_is_user_liked':like.is_user_liked,'blog_obj':blog_serializer.data})
                
                # print('Header Token ', header_token)
                # print('Vue terefden axiosdan POST request geldi yoxlama ucun')
                # print('Method Value ', self.request.method)
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

@csrf_exempt
def searchBlogView(request):
    result = get_csrf_token(request)
    csrfmiddlewaretoken_django = json.loads(result.getvalue())['token']
    print('noldu amk burda')
    if request.method == 'POST' and result and csrfmiddlewaretoken_django !='':
        request_values = [i for i in request.POST]
        request_value = json.loads(request_values[0])
        csrfmiddlewaretoken_vuejs = request_value['csrfmiddlewaretoken']
        searched_post_text = request_value['searched_post_text']
        if searched_post_text != '':
            find_blog = Blog.objects.filter(title__icontains=searched_post_text)
            serializer_find_blog = BlogSerializer(find_blog,many=True)
            
            
            # user = Token.objects.get(key=request_value['logged_user_token']).user
            profile = Profile.objects.all()
            profile_serializer = ProfileSerializer(profile,many=True)
            print('Serializer find blog  ', type(serializer_find_blog.data))
        return JsonResponse({'find_blog':serializer_find_blog.data,'profile_serializer':profile_serializer.data},safe=True)
    
    return HttpResponse('neyse axi get de isledi')
    