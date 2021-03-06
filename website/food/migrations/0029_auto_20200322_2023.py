# Generated by Django 3.0.4 on 2020-03-22 20:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0028_auto_20200322_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date_expiry',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 20, 23, 25, 389806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='unit',
            field=models.CharField(choices=[('unit(s)', 'UN'), ('bag(s)', 'BG'), ('bottle(s)', 'BT'), ('box(s)', 'BX'), ('can(s)', 'CN'), ('carton(s)', 'CA'), ('jar(s)', 'JR'), ('package(s)', 'PK'), ('gram(s)', 'GR'), ('kilo(s)', 'KG'), ('liter(s)', 'LT')], default='unit(s)', max_length=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='use_before',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 20, 23, 25, 389848, tzinfo=utc)),
        ),
    ]
