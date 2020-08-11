from django.contrib import admin

from .models import Album, Post, Todo

admin.site.register(Album)
admin.site.register(Post)
admin.site.register(Todo)
