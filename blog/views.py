from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# def home(request):
#     context = {}
#     return render(request, 'blog/main.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'blog/main.html'
    ordering = ['-date_created']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/articles_details.html'


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    #fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = PostForm
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
