# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnm_guide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.URLField(),
        ),
    ]
