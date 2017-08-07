# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-05 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170805_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('details', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
