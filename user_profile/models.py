from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.
#!Profile
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profilepicture',validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True)
    slug = models.SlugField(unique=True,db_index=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.user)
        super(Profile,self).save(*args,**kwargs)
    
    @property
    def get_absolute_url(self):
        return f"profile/{self.slug}/"
    
    @property
    def get_profile_picture(self):
        if self.profile_picture:
            return f"http://127.0.0.1:8000{self.profile_picture.url}"
        #else
        return ''
    
    @property
    def getAllProfile(self):
        return Profile.objects.all()
    
    class Meta:
        ordering = ['-created']
        verbose_name='Profile'
        verbose_name_plural='Profiles'

#?create_profile_for_user
def create_profile_for_user(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile_for_user,sender=User)