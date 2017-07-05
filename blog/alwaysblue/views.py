# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Blog, Tag, Author, Images

from django.shortcuts import render_to_response, get_object_or_404

from BeautifulSoup import BeautifulSoup

import django_markdown

# Create your views here.


def home(request):
    posts = Blog.objects.all()[:10]
    for post in posts:
        html = django_markdown.utils.markdown(value=post.body)
        soup = BeautifulSoup(html)
        try:
            ex = soup.p.string
            imgs = soup.findAll('img', {'src': True})
            if len(imgs) > 1:
                post.type = 4
            for img in imgs:
                url = img['src']
                imglist = Images.objects.filter(link=url)
                if len(imglist) == 0:
                    image = Images(link=url)
                    image.save()
                else:
                    image = imglist[0]
                post.imagelinks.add(image)
            post.save()
            post.excerpt = ex[0:330] + '...'
            post.save()
        except:
            pass



    return render_to_response('alwaysblue/index.html', {
        'tags': Tag.objects.all(),
        'posts': posts
    })


def index(request):
    posts = Blog.objects.all()
    for post in posts:
        html = django_markdown.utils.markdown(value=post.body)
        print html
        soup = BeautifulSoup(html)
        try:
            ex = soup.p.string
            print 'hello'
            post.excerpt = ex[0:330] + '...'
            post.save()
        except:
            pass

    return render_to_response('alwaysblue/index1.html', {
        'tags': Tag.objects.all(),
        'posts': posts[:10]
    })


def view_post(request, slug):
    object = get_object_or_404(Blog, slug=slug)
    if object.type == 0:
        return render_to_response('alwaysblue/single-standard.html', {
            'post': object
        })
    elif object.type == 1:
        return render_to_response('alwaysblue/single-standard.html', {
            'post': object
        })
    elif object.type == 3:
        return render_to_response('alwaysblue/single-audio.html', {
            'post': object
        })
    elif object.type == 4:
        return render_to_response('alwaysblue/single-standard.html', {
            'post': object
        })
    elif object.type == 6:
        return render_to_response('alwaysblue/single-video.html', {
            'post': object
        })


def view_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    return render_to_response('alwaysblue/tag.html', {
        'tag': tag,
        'posts': Blog.objects.filter(tags=tag)[:5]
    })


def view_author(request, slug):
    author = get_object_or_404(Author, slug=slug)
    return render_to_response('alwaysblue/view_author.html', {
        'author': author,
        'posts': Blog.objects.filter(author=author)[:5]
    })


def view_login(request):
    return render(request, 'alwaysblue/login.html')

