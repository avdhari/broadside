from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *

# def home(request):
#     context = {}
#     return render(request, 'blog/main.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'blog/main.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/articles_details.html'


class CreatePost(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = '__all__'