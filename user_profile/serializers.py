from rest_framework import serializers

from .models import *

#!ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    profile_category = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    profile_comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id','user','bio','profile_picture','slug','posts','profile_category','profile_comments']
        
        