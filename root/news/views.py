from django.shortcuts import render
from .models import Post


def blog(request):
    all_posts = Post.objects.all()
    return render(request, 'news/blog.html', context={
        'all_posts': all_posts
    })
