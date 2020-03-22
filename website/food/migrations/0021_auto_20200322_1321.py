# Generated by Django 3.0.4 on 2020-03-22 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0020_auto_20200322_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date_expiry',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 13, 21, 17, 59066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='use_before',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 13, 21, 17, 59110, tzinfo=utc)),
        ),
    ]
