from django.shortcuts import render, get_object_or_404, redirect
from images.models import FeaturedImage, GalleryImage, WebsiteImage, FrontPageImage, AbstractImage, NatureImage, UrbanImage, VermontImage
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    logos = WebsiteImage.objects.all()
    images = FrontPageImage.objects.all() 
    print(settings.STATIC_ROOT)
    return render(request, 'images/home.html',
                              { 'logos' : logos, 'images' : images})

def about(request):
	images = GalleryImage.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/about.html', {'images' : images, 'logos' : logos})


def gallery(request, gallery_cat):
	if(gallery_cat == "abstract"):
		images = AbstractImage.objects.all().order_by('order')
	elif(gallery_cat == "nature"):
		images = NatureImage.objects.all().order_by('order')
	elif(gallery_cat == "urban"):
		images = UrbanImage.objects.all().order_by('order')		
	elif(gallery_cat == "vermont"):
		images = VermontImage.objects.all().order_by('order')				
	else: images = AbstractImage.objects.all().order_by('order')

	logos = WebsiteImage.objects.all()

	return render(request, 'images/gallery.html', {'images': images, 'logos': logos, 'gallery_cat' : gallery_cat})

def gimage(request, image_cat, image):
	if(image_cat == "abstract"):
		page_image = AbstractImage.objects.get(name__exact = image)
	elif(image_cat == "nature"):
		page_image = NatureImage.objects.get(name__exact = image)
	elif(image_cat == "urban"):
		page_image = UrbanImage.objects.get(name__exact = image)
	elif(image_cat == "vermont"):
		page_image = VermontImage.objects.get(name__exact = image)			

	logos = WebsiteImage.objects.all()
	return render(request, 'images/image.html', {'image' : page_image, 'logos' : logos})


