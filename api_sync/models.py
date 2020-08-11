from django.db import models


class Todo(models.Model):
    userId = models.IntegerField(default=0)
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=4000)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Album(models.Model):
    userId = models.IntegerField(default=0)
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=4000)

    def __str__(self):
        return self.title


class Post(models.Model):
    userId = models.IntegerField(default=0)
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=4000)
    body = models.TextField()

    def __str__(self):
        return self.title
