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
        input_formats=['%Y-%m-%d'],
        # attrs={'id': 'date_purchased'}
        # widget=FengyuanChenDatePickerInput()
        )
        
    date_expiry = forms.DateField(
        input_formats=['%Y-%m-%d'],
        # attrs={'id': 'date_expiry'}
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
        input_formats=['%Y-%m-%d'],
        # attrs={'id': 'use_before'}
        # required=False,
        # auto_now=False, 
        # auto_now_add=False,
        # default=now()+timedelta(days=7),
        )