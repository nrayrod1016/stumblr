from django.shortcuts import render

# Create your views here.

def home(request): 
  return render(request, 'home.html')


def about(request): 
  return render(request, 'about.html')

def posts_index(request): 
  return render(request, 'posts/index.html', )
  #  { 'posts': posts}


def posts_detail(request): 
  return render(request, 'posts/detail.html')

  