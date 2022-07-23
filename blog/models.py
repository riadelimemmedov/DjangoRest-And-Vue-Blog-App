from django.db import models

from user_profile.models import *
from django.core.validators import FileExtensionValidator

# Create your models here.

#!Blog
class Blog(models.Model):
    title = models.CharField(max_length=100,blank=False)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(Profile,related_name='posts',on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='blogpicture',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
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

#!Categorys
class Category(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    owner = models.ForeignKey(Profile,related_name='profile_category',on_delete=models.CASCADE,blank=False)
    blogs = models.ForeignKey(Blog,related_name='blog_category',on_delete=models.CASCADE,blank=False)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'