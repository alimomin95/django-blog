# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Blog, Tag, Author, Images

from django_markdown.admin import MarkdownModelAdmin

# Register your models here.


class BlogAdmin(MarkdownModelAdmin):
    exclude = ['posted', 'excerpt']
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Images)
