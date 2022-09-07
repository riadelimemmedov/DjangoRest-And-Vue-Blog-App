from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

#!BlogSerializer
class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user',read_only=True)
    liked = serializers.StringRelatedField(read_only=True,many=True)
    #currentuser = serializers.CharField(source='currentuser.username',read_only=True)
    # user = serializers.SerializerMethodField(method_name='get_current_user')
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #current_user = serializers.StringRelatedField(read_only=True,default=serializers.CurrentUserDefault())   
    #blog_category = serializers.PrimaryKeyRelatedField(many=True,queryset=Category.objects.filter(id=1))
    #category = serializers.PrimaryKeyRelatedField(read_only=True,source='category.name')
    #blog_comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    
    # def get_current_user(self,obj):
    #     request = self.context.get('request',None)
    #     if request:
    #         print('Request User Value ', request.user)
    #         return request.user
        
    class Meta:
        model = Blog
        fields = ['id','title','body','owner','blog_image','slug','created','updated','category','blog_comments','liked','is_liked']


    
#!CategorySerializers
class CategoryBlogSerializer(serializers.ModelSerializer):
    #owner = serializers.CharField(source='owner.user',read_only=True)
    #blogs = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    
    class Meta:
        model = CategoryBlog
        fields = ['id','slug']
        

#!CommentSerializer 
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = CommentBlog
        fields = ['body','blog','owner']

#!UserSerilizers
class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']