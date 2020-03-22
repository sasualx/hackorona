from django import forms
from django.utils.timezone import now, timedelta

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

class FoodForm(forms.Form):  

    name = forms.CharField(
        # required=True,
        max_length=30
        )
    number = forms.DecimalField(
        # required=True,
        max_digits=5, 
        decimal_places=2
        )
    unit = forms.ChoiceField(
        # required=True,
        choices=UNIT_CHOICES,
        # default=UNIT
        )
    date_purchased = forms.DateField(
        required=False,
        # auto_now=False,
        # auto_now_add=False,
        # default=now
        )
    date_expiry = forms.DateField(
        # required=False,
        # auto_now=False, 
        # auto_now_add=False,
        # default=now()+timedelta(days=30),
        )
    status = forms.ChoiceField(
        # required=True,
        choices=FRESHNESS_CHOICES,
        # default=FRESH,
        )
    use_before = forms.DateField(
        # required=False,
        # auto_now=False, 
        # auto_now_add=False,
        # default=now()+timedelta(days=7),
        )