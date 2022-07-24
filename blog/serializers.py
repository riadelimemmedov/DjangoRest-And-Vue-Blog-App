from rest_framework import serializers

from .models import *

#!BlogSerializer
class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user',read_only=True)
    #blog_category = serializers.PrimaryKeyRelatedField(many=True,queryset=Category.objects.filter(id=1))
    category = serializers.PrimaryKeyRelatedField(read_only=True,source='category.name')
    blog_comments = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    class Meta:
        model = Blog
        fields = ['title','body','owner','blog_image','slug','created','updated','category','blog_comments']

#!CategorySerializers
class CategoryBlogSerializer(serializers.ModelSerializer):
    #owner = serializers.CharField(source='owner.user',read_only=True)
    #blogs = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    
    class Meta:
        model = CategoryBlog
        fields = ['id','slug']
        

#!CommentSerializer 
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='profile.user',read_only=True)
    
    class Meta:
        model = CommentBlog
        fields = ['id','body','owner','blog']