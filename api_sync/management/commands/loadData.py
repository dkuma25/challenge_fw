import requests

from django.core.management.base import BaseCommand, CommandError
from api_sync.models import Album, Post, Todo


class Command(BaseCommand):
    help = 'Populate db with Api Data'

    def add_arguments(self, parser):
        parser.add_argument('--all', '-a', action='store_true', dest='all', default=False)
        parser.add_argument('--post', action='store_true', dest='post', default=False)
        parser.add_argument('--album', action='store_true', dest='album', default=False)
        parser.add_argument('--todo', action='store_true', dest='todo', default=False)

    def handle(self, *args, **options):
        def get_json(_url=None):
            if not _url:
                return []
            response = requests.get(_url)
            return response.json() or []
        base_url = 'https://jsonplaceholder.typicode.com'
        try:
            if options['all'] or options['album']:
                print('Loading Albums...')
                json = get_json(base_url+'/albums')
                album_list = list()
                for album in json:
                    userId = album['userId'] or None
                    id = album['id'] or None
                    title = album['title'] or None
                    if None not in (userId, id, title):
                        album_list.append(Album(userId=userId, id=id, title=title))
                Album.objects.bulk_create(album_list)
            if options['all'] or options['post']:
                print('Loading Posts...')
                json = get_json(base_url+'/posts')
                post_list = list()
                for post in json:
                    userId = post['userId'] or None
                    id = post['id'] or None
                    title = post['title'] or None
                    body = post['body'] or None
                    if None not in (userId, id, title, body):
                        post_list.append(Post(userId=userId, id=id, title=title, body=body))
                Post.objects.bulk_create(post_list)
            if options['all'] or options['todo']:
                print('Loading Todos...')
                json = get_json(base_url+'/todos')
                todo_list = list()
                for todo in json:
                    userId = todo['userId'] or None
                    id = todo['id'] or None
                    title = todo['title'] or None
                    completed = todo['completed'] or False
                    if None not in (userId, id, title):
                        todo_list.append(Todo(userId=userId, id=id, title=title, completed=completed))
                Todo.objects.bulk_create(todo_list)
        except Exception as e:
            CommandError('Error: {}'.format(e))
            print(e)
        self.stdout.write('Data successfully loaded.')