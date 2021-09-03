from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 



# Create your models here.


STATUS = ( 
  (0, 'Draft'),
  (1, 'Publish')
)

class Post(models.Model): 
  title = models.CharField(max_length=100, unique=True)
  author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
  content = models.TextField()
  create_time = models.DateTimeField(auto_now_add=True)
  update_time = models.DateField(auto_now=True)
  

  class Meta: 
    ordering = ['-create_time'] 

  def __str__(self): 
    return self.title 


  def get_absolute_url(self): 
    return reverse('posts_detail', kwargs={'post_id': self.id})




class Comment(models.Model): 
  post = models.ForeignKey(Post,on_delete=models.CASCADE,name='comments')
  author = models.CharField(max_length=80)
  content = models.TextField()
  create_time = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=False)

  class Meta: 
    ordering = ['create_time']

  def __str__(self): 
    return 'Comment {} by {}'.format(self.body, self.author)