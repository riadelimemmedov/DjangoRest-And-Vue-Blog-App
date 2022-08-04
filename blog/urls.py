from django.urls import path

from .views import *

app_name='blog'
urlpatterns = [
    path('',BlogListCreateView.as_view(),name='BlogListCreateView'),
    path('blog-detail/<int:pk>/',BlogDetailView.as_view(),name='BlogDetailView'),
    path('category-blogs/',CategoryBlogListCreateView.as_view(),name='CategoryListCreateView'),
    path('comment-blogs/',CommentBlogListCreateView.as_view(),name='CommentBlogListCreateView'),
    path('comment-blog/<int:pk>/',CommentBlogDetail.as_view(),name='CommentBlogDetail')
]

