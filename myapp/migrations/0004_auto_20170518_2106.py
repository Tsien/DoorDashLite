# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170518_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='instructions',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='subtotal',
            field=models.IntegerField(default=0),
        ),
    ]
