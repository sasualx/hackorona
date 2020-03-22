from django import forms
from django.utils.timezone import now, timedelta

FRESH = 'Fresh'
EXPIRING = 'Expiring'

FRESHNESS_CHOICES = [
    (FRESH, 'Fresh'),
    (EXPIRING, 'Expiring'),
]

UNIT = 'unit(s)'
BAG = 'bag(s)'
BOTTLE = 'bottle(s)'
BOX = 'box(s)'
CAN = 'can(s)'
CARTON = 'carton(s)'
JAR = 'jar(s)'
PACKAGE = 'package(s)'
GRAM = 'gram(s)'
KILOGRAM = 'kilo(s)'
LITER = 'liter(s)'

UNIT_CHOICES = [
    (UNIT, 'unit'),
    (BAG, 'bag'),
    (BOTTLE, 'bottle'),
    (BOX, 'box'),
    (CAN, 'can'),
    (CARTON, 'carton'),
    (JAR, 'jar'),
    (PACKAGE, 'package'),
    (GRAM, 'g'),
    (KILOGRAM, 'kg'),
    (LITER, 'liter'),
]  


class FoodForm(forms.Form):  

    name = forms.CharField(
        max_length=30
        )
    number = forms.DecimalField(
        max_digits=5, 
        decimal_places=2
        )
    unit = forms.ChoiceField(
        choices=UNIT_CHOICES,
        )
    date_purchased = forms.DateField(
        input_formats=['%Y-%m-%d'],
        initial=now(),
        )
        
    date_expiry = forms.DateField(
        input_formats=['%Y-%m-%d'],
        initial=now()+timedelta(days=30),
        )
    status = forms.ChoiceField(
        choices=FRESHNESS_CHOICES,
        initial=FRESH
        )
    use_before = forms.DateField(
        input_formats=['%Y-%m-%d'],
        initial=now()+timedelta(days=7),
        )

