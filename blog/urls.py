from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('artice/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('newpost/', CreatePost.as_view(), name="create-post"),

]
 