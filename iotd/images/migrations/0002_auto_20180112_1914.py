# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='featuredimage',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
