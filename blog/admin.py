from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Blog)
admin.site.register(CategoryBlog)
admin.site.register(CommentBlog)
admin.site.register(Like)