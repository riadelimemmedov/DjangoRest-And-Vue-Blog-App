from django.urls import path

from .views import *

app_name='blog'
urlpatterns = [
    path('',BlogListCreateView.as_view(),name='BlogListCreateView'),
    path('categories/',CategoryListCreateView.as_view(),name='CategoryListCreateView')
]
