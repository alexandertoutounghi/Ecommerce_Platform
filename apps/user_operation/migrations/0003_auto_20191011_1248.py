# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-11 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20191010_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='post_code',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='district',
            field=models.CharField(default='', max_length=100, verbose_name='District'),
        ),
    ]
