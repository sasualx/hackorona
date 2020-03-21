from django.db import models


class Post(models.Model):
    position_x = models.PositiveIntegerField()
    position_y = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)