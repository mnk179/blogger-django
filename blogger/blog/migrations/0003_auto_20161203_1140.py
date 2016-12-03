# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161203_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_edit_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date last edited'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
    ]
