# Generated by Django 3.0.4 on 2020-03-21 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20200321_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date_expiry',
            field=models.DateField(default=datetime.datetime(2020, 4, 20, 20, 44, 22, 589413, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='use_before',
            field=models.DateField(default=datetime.datetime(2020, 3, 28, 20, 44, 22, 589455, tzinfo=utc)),
        ),
    ]
