# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-31 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_auto_20170331_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='numOfStudentsPrimary',
            field=models.IntegerField(default=434),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='numOfStudentsSeconadry',
            field=models.IntegerField(default=207),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='numOfStudentsSenior',
            field=models.IntegerField(default=422),
        ),
    ]
