# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models import permalink

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ManyToManyField('alwaysblue.Category')
    embed_video = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})



@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})