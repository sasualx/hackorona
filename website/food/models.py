from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta

class Food(models.Model):

    FRESH = 'FR'
    EXPIRING = 'EX'

    FRESHNESS_CHOICES = [
        (FRESH, 'Fresh'),
        (EXPIRING, 'Expiring soon'),
    ]

    UNIT = 'UN'
    BAG = 'BG'
    BOX = 'BX'
    CAN = 'CN'
    CARTON = 'CA'
    JAR = 'JR'
    PACKAGE = 'PK'
    GRAM = 'GR'
    KILOGRAM = 'KG'
    LITER = 'LT'
  
    UNIT_CHOICES = [
        (UNIT, 'unit(s)'),
        (BAG, 'bag(s)'),
        (BOX, 'box(es)'),
        (CAN, 'can(s)'),
        (CARTON, 'carton(s)'),
        (JAR, 'jar(s)'),
        (PACKAGE, 'package(s)'),
        (GRAM, 'gram(s)'),
        (KILOGRAM, 'kilogram(s)'),
        (LITER, 'liter(s)'),
    ]    

    user = models.OneToOneField(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=30, 
        blank=True
        )
    number = models.DecimalField(
        default=1, 
        max_digits=5, 
        decimal_places=2
        )
    unit = models.CharField(
        max_length=2, 
        choices=UNIT_CHOICES,
        default=UNIT,
        )
    date_purchased = models.DateField(
        auto_now=False, 
        auto_now_add=False, 
        default=now
        )
    date_expiry = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        default=now
        )
    status = models.CharField(
        max_length=2,
        choices=FRESHNESS_CHOICES,
        default=FRESH,
        )
    use_before = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        default=now()+timedelta(days=7),
        )

# Create your models here.
