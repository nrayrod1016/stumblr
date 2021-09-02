from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request): 
  return render(request, 'home.html')


def about(request): 
  return render(request, 'about.html')

def posts_index(request):
  posts = Post.objects.all() 
  return render(request, 'posts/index.html', { 'posts': posts} )
 


def posts_detail(request, post_id): 
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', { 'post': post})


class PostCreate(CreateView): 
  model = Post
  fields = ['title', 'author', 'content' ]

  def form_valid(self, form): 
    form.instance.user = self.request.user
    return super().form_valid(form)

class PostUpdate(UpdateView): 
  model = Post 
  fields = ['title', 'author', 'content', ]

class PostDelete(DeleteView): 
  model = Post 
  success_url = '/posts/' 