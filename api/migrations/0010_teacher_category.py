# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-24 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20170322_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='category',
            field=models.CharField(default='primary', max_length=200),
            preserve_default=False,
        ),
    ]