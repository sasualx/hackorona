# Generated by Django 3.0.4 on 2020-03-22 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0024_auto_20200322_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date_expiry',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 18, 15, 7, 806795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='use_before',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 18, 15, 7, 806843, tzinfo=utc)),
        ),
    ]
