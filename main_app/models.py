from django.db import models

# Create your models here.
STATUS = ( 
  (0, 'Draft'),
  (1, 'Publish')
)

class Post(models.Model): 
  title = models.CharField(max_length=100, unique=True)
  author = models.CharField(max_length=100, unique=True)
  content = models.TextField()
  create_time = models.DateTimeField(auto_now_add=True)
  update_time = models.DateField(auto_now=True)
  

  class Meta: 
    ordering = ['-create_time'] 

  def __str__(self): 
    return self.title 