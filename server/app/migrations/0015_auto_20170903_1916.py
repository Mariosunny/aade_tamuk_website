# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-03 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20170903_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
