# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161207_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
            ],
        ),
    ]
