from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render, redirect,get_object_or_404 
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic 
from .forms import CommentForm 
# Create your views here.
from django.contrib.auth.views import LoginView 

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
  

def add_comment(request, post_id):
  # post = get_object_or_404(Post)
  # 
  # comments = Post.comments.filter(active=True) 
  new_comment = None 
  form = CommentForm(request.POST)
  if form.is_valid(): 
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.save() 
  else: 
    form = CommentForm() 
  return redirect('posts_detail', post_id=post_id)
  
class Home(LoginView): 
  template_name = 'home.html'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('posts_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
