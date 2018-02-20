# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_abstractimages_natureimages_urbanimages_vermontimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('category_id', models.CharField(max_length=200)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NatureImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('category_id', models.CharField(max_length=200)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UrbanImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('category_id', models.CharField(max_length=200)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='VermontImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('category_id', models.CharField(max_length=200)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='AbstractImages',
        ),
        migrations.DeleteModel(
            name='NatureImages',
        ),
        migrations.DeleteModel(
            name='UrbanImages',
        ),
        migrations.DeleteModel(
            name='VermontImages',
        ),
    ]