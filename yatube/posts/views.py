
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    templates = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, templates, context)


def group_posts(request, slug):
    templates = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    text = 'Записи сообщества'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'text': text
    }
    return render(request, templates, context)
