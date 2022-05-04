from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    templates = 'posts/index.html'
    return render(request, templates)


def group_posts(request):
    return HttpResponse('Посты и статьи')