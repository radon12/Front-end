# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebarapp', '0002_olduser_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(max_length=10),
        ),
    ]
