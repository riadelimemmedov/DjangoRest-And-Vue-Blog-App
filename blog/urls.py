from django.urls import path

from .views import *

app_name='blog'
urlpatterns = [
    path('',BlogListCreateView.as_view(),name='BlogListCreateView'),
    path('category-blogs/',CategoryBlogListCreateView.as_view(),name='CategoryListCreateView'),
    path('comment-blogs/',CommentBlogListCreateView.as_view(),name='CommentBlogListCreateView'),
    path('comments-blog/<int:pk>/',CommentBlogDetail.as_view(),name='CommentBlogDetail')
]

