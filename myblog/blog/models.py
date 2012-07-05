# Create your models here.
from django.db import models
from django.contrib import admin
class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateField()
    updated=models.DateField()
    def __unicode__():
        return self.body

class Comment(models.Model):
    post=models.ForeignKey(Post)
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField()
    updated=models.DateField()
    def __unicode__():
        return self.author
admin.site.register(Post)
admin.site.register(Comment)
