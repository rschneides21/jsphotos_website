from django.db import models

# Create your models here.

#create abstract base classes for images


class AbstractImage(models.Model):
	name = models.CharField(max_length=200)
	order = models.IntegerField()
	category_id = models.CharField(max_length=200)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class NatureImage(models.Model):
	name = models.CharField(max_length=200)
	order = models.IntegerField()
	category_id = models.CharField(max_length=200)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class UrbanImage(models.Model):
	name = models.CharField(max_length=200)
	order = models.IntegerField()
	category_id = models.CharField(max_length=200)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class VermontImage(models.Model):
	name = models.CharField(max_length=200)
	order = models.IntegerField()
	category_id = models.CharField(max_length=200)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class WebsiteImage(models.Model):

	name = models.CharField(max_length=200)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class FrontPageImage(models.Model):

	name = models.CharField(max_length=200)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")
