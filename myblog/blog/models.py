# Create your models here.
from django.db import models
from django.contrib import admin


class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateField()
    updated=models.DateField()
    def __unicode__(self):
        return self.body

class Comment(models.Model):
    post=models.ForeignKey(Post)
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField()
    updated=models.DateField()
    def __unicode__(self):
        return self.author


class PostAdmin(admin.ModelAdmin):
    list_display=('title','created','updated')
    search_fields=('title','body')
    list_filter=('title','created')
    def title_first_10(self):
        return self.title[:10]

class CommentAdmin(admin.ModelAdmin):
    list_display=('post','author','body','created','updated')
    list_filter=('author','created')
    def title_first_60(self):
        return self.title[:60]

class CommentInline(admin.TabularInline):
  model=Comment
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

