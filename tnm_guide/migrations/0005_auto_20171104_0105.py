# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnm_guide', '0004_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='resource',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='resources_images'),
        ),
    ]
