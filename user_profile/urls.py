from django.urls import path
from .views import *


app_name = 'user_profile'
urlpatterns = [
    path('profile/',ProfileListCreateView.as_view(),name='ProfileSerializer'),
    path('update/profile/<slug:slug>/',ProfileUpdateView.as_view(),name='updateProfile')
]
