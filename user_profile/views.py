from django.http import Http404, JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import generics,response,status
from rest_framework.views import APIView


from .serializers import *
from .models import *

# Create your views here.
#!ProfileListCreateView
class ProfileListCreateView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@method_decorator(csrf_exempt,name='dispatch')
class ProfileUpdateView(APIView):
    def get_object(self,slug):
        try:
            return Profile.objects.get(slug=slug)
        except Profile.DoesNotExist:
            raise Http404

    def get(self,request,slug,format=None):
        print('Slug value ', slug)
        profile = self.get_object(slug)
        serializer_profile = ProfileSerializer(profile)
        return response.Response(serializer_profile.data,status=status.HTTP_200_OK)

    def post(self,request,slug,format=None):
        print('firstname ', request.data['firstname'])
        print('lastname ', request.data['lastname'])
        print('organization_name ', request.data['organization_name'])
        print('location ', request.data['location'])
        print('email_address ', request.data['email_address'])
        print('bio ', request.data['bio']) 
        
        
        profile = Profile.objects.filter(slug=slug).update(
            firstname=request.data['firstname'],
            lastname=request.data['lastname'],
            organization_name=request.data['organization_name'],
            email_address=request.data['email_address'],
            location=request.data['location'],
            bio = request.data['bio']
        )
        print('profile updated ', profile)
        return response.Response({'success': True})