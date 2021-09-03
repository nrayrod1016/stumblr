from django.shortcuts import render, redirect 
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic 
from .forms import CommentForm 
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
  comment_form = CommentForm() 
  return render(request, 'posts/detail.html', { 'post': post, 'comment_form': comment_form})


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
  

def comment(request, post_id): 
  form = CommentForm(request.POST)
  if form.is_valid(): 
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.save() 
  return redirect('post_detail', post_id=post_id)
  


# class PostList(generic.ListView): 
#   model = Post 
#   queryset = Post.ojects.filter(status=1).order_by('create_time')
#   template_name = 'home.html'