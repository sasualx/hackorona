from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Food(models.Model):

    FRESH = 'FR'
    EXPIRING = 'EX'

    FRESHNESS_CHOICES = [
        (FRESH, 'Fresh'),
        (EXPIRING, 'Expiring soon'),
    ]

    user = models.OneToOneField(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    number = models.IntegerField(default=1)
    unit = models.CharField(max_length=10, blank=True)
    date_purchased = models.DateField(auto_now=False, auto_now_add=False, default=now)
    date_expiry = models.DateField(auto_now=False, auto_now_add=False,default=now)
    status = models.CharField(
        max_length=2,
        choices=FRESHNESS_CHOICES,
        default=FRESH,
        )

# Create your models here.
