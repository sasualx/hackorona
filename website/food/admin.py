from __future__ import absolute_import

from django.contrib import admin
from website.food.models import Food

@admin.register(Food)
class PostAdmin(admin.ModelAdmin):
    pass
