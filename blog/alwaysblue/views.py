# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Blog, Category, Author

from django.shortcuts import render_to_response, get_object_or_404
# Create your views here.


def home(request):
    return render_to_response('alwaysblue/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:10]
    })


def index(request):
    return render_to_response('alwaysblue/index1.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:10]
    })


def view_post(request, slug):
    return render_to_response('alwaysblue/view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('alwaysblue/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })


def view_author(request, slug):
    author = get_object_or_404(Author, slug=slug)
    return render_to_response('alwaysblue/view_author.html', {
        'author': author,
        'posts': Blog.objects.filter(author=author)[:5]
    })
