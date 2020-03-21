from __future__ import absolute_import

from django.contrib import admin
from website.posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
