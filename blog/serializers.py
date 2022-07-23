from rest_framework import serializers

from .models import *

#!BlogSerializer
class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user',read_only=True)
    blog_category = serializers.PrimaryKeyRelatedField(many=True,queryset=Category.objects.filter(id=1))
    
    class Meta:
        model = Blog
        fields = ['title','body','owner','blog_image','slug','created','updated','blog_category']

#!CategorySerializers
class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user',read_only=True)
    #blogs = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    
    class Meta:
        model = Category
        fields = ['id','name','owner','blogs']
        
        