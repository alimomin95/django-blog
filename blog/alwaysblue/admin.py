# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Blog, Category, Author

from django_markdown.admin import MarkdownModelAdmin

# Register your models here.


class BlogAdmin(MarkdownModelAdmin):
    exclude = ['posted']
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
