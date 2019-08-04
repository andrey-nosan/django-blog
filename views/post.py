from django.shortcuts import render

from blog.models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def show(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    tags = post.tags.all()
    return render(request, 'blog/show.html', context={'post': post, 'tags': tags})
