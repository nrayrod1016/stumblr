from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Comment, Profile



class ProfileInline(admin.StackedInline): 
  model = Profile 
  can_delete = False 
  verbose_name_plural = 'Profile' #each user will have only one profile
  fk_name = 'user'

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)