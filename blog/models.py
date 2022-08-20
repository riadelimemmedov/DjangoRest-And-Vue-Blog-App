import json
from re import S
from django.db import models
from django.utils.text import slugify
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


from user_profile.models import *
from django.core.validators import FileExtensionValidator

# Create your models here.

#!Categorys
class CategoryBlog(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    slug = models.SlugField(max_length=100,db_index=True,blank=True,unique=True)
    
    def __str__(self):
        return str(self.name)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(CategoryBlog,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'CategoryBlog'
        verbose_name_plural = 'CategoryBlogs'

#!Blog
class Blog(models.Model):
    title = models.CharField(max_length=100,blank=False)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(Profile,related_name='posts',on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='blogpicture',validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True,null=True)
    category = models.ForeignKey(CategoryBlog,related_name='category_post',on_delete=models.CASCADE,blank=True,null=True)
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    is_liked = models.BooleanField(default=False)
    currentuser = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='currentuser',on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,db_index=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)
    
    #Bura get_absolute_url(self): elave edersen sonra single postlar ucun
    def get_absolute_url(self):
        return f"blog-detail/{self.id}/"


    #!Burda her bloga gore likelarin sayini donduren kodu yaz
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
#!CommentBlog
def get_current_user(request):
    return request.user         
class CommentBlog(models.Model):
    body = models.TextField(blank=False)
    blog = models.ForeignKey(Blog,related_name='blog_comments',on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile,related_name='profile_comments',on_delete=models.CASCADE,default=get_user_model())
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Comments To - {self.blog.title}"
    class Meta:
        ordering = ['-created']
        verbose_name = 'CommentBlog'
        verbose_name_plural = 'CommentBlogs'
        

#!Like
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User,related_name='profile_like',on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,related_name='blog_like',on_delete=models.CASCADE)
    is_user_liked = models.BooleanField(default=False)
    value = models.CharField(max_length=100,choices=LIKE_CHOICES,default='Like')
    
    def __str__(self):
        return str(self.value)
    
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
