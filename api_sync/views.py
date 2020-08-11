from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Album, Post, Todo


class PostView(generic.DetailView):
    model = Post
    template_name = 'api_sync/post.html'


def index(request):
    album_list = Album.objects.all()
    post_list = Post.objects.all()
    todo_list = Todo.objects.all()

    return render(request, 'api_sync/index.html', {
        'album_list': album_list,
        'post_list': post_list,
        'todo_list': todo_list
    })



