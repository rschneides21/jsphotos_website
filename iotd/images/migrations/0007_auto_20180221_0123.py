# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 01:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20180220_2036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeaturedImage',
        ),
        migrations.DeleteModel(
            name='GalleryImage',
        ),
    ]
