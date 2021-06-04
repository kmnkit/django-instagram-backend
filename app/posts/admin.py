from django.contrib import admin
from .models import Comment, Hashtag, Post

admin.site.register(Hashtag)
admin.site.register(Post)
admin.site.register(Comment)