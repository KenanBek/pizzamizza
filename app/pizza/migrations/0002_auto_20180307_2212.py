# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-07 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.PositiveSmallIntegerField(choices=[(30, '30 Centimeters'), (50, '50 Centimeters')]),
        ),
    ]