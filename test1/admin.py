from django.contrib import admin
from test1.models import Category, Post, Comment
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
