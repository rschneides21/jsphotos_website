from django.db import models

# Create your models here.

#create abstract base classes for images

class FeaturedImage(models.Model):

    name = models.CharField(max_length=200)
    tagline = models.TextField()
    uploaded = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="") 

class GalleryImage(models.Model):

	name = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class AbstractImages(models.Model):
	name = models.CharField(max_length=200)
	order = models.CharField(max_length=100)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class NatureImages(models.Model):
	name = models.CharField(max_length=200)
	order = models.CharField(max_length=100)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class UrbanImages(models.Model):
	name = models.CharField(max_length=200)
	order = models.CharField(max_length=100)
	uploaded = models.DateTimeField(auto_now=True)
	img = models.ImageField(upload_to="")

class VermontImages(models.Model):
	name = models.CharField(max_length=200)
	order = models.CharField(max_length=100)
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
