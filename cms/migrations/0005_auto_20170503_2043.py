# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-03 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20170503_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='contenu_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='module',
            name='evaluation_published',
            field=models.BooleanField(default=False),
        ),
    ]
