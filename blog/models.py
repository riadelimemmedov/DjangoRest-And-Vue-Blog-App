from re import S
from django.db import models
from django.utils.text import slugify

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
    blog_image = models.ImageField(upload_to='blogpicture',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    category = models.ForeignKey(CategoryBlog,related_name='category_post',on_delete=models.CASCADE,null=True)
    slug = models.SlugField(unique=True,db_index=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)
    
    #Bura get_absolute_url(self): elave edersen sonra single postlar ucun
    @property
    def get_absolute_url(self):
        return f"blog/{self.slug}/"
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
#!CommentBlog
class CommentBlog(models.Model):
    body = models.TextField(blank=False)
    blog = models.ForeignKey(Blog,related_name='blog_comments',on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile,related_name='profile_comments',on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments To - {self.blog.title}"
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'CommentBlog'
        verbose_name_plural = 'CommentBlogs'
    
    
