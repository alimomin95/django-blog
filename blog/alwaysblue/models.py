# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models import permalink

from django_markdown.models import MarkdownField

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_tag', None, {'slug': self.slug})


@python_2_unicode_compatible
class Author(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_author', None, {'slug': self.slug})


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.IntegerField(default=0)
    body = MarkdownField()
    excerpt = models.TextField(blank=True, null=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author)
    embed_video = models.CharField(max_length=200, null=True, blank=True)
    published = models.BooleanField(default=True)
    audio = models.FileField(upload_to='audio', null=True, blank=True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

