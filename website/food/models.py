from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta

class Food(models.Model):

    FRESH = 'Fresh'
    EXPIRING = 'Expiring'

    FRESHNESS_CHOICES = [
        (FRESH, 'FR'),
        (EXPIRING, 'EX'),
    ]

    UNIT = 'unit(s)'
    BAG = 'bag(s)'
    BOX = 'box(s)'
    CAN = 'can(s)'
    CARTON = 'carton(s)'
    JAR = 'jar(s)'
    PACKAGE = 'package(s)'
    GRAM = 'gram(s)'
    KILOGRAM = 'kilo(s)'
    LITER = 'liter(s)'
  
    UNIT_CHOICES = [
        (UNIT, 'UN'),
        (BAG, 'BG'),
        (BOX, 'BX'),
        (CAN, 'CN'),
        (CARTON, 'CA'),
        (JAR, 'JR'),
        (PACKAGE, 'PK'),
        (GRAM, 'GR'),
        (KILOGRAM, 'KG'),
        (LITER, 'LT'),
    ]    

    user = models.ManyToManyField(User)
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
        max_length=10, 
        choices=UNIT_CHOICES,
        default=UNIT
        )
    date_purchased = models.DateField(
        auto_now=False, 
        auto_now_add=False, 
        default=now
        )
    date_expiry = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        default=now()+timedelta(days=30),
        )
    status = models.CharField(
        max_length=10,
        choices=FRESHNESS_CHOICES,
        default=FRESH,
        )
    use_before = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        default=now()+timedelta(days=7),
        )

# Create your models here.
