# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170803_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', height_field=100, upload_to='post', width_field=70),
        ),
    ]
