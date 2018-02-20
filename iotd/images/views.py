from django.shortcuts import render, get_object_or_404, redirect
from images.models import FeaturedImage, GalleryImage, WebsiteImage, FrontPageImage, AbstractImages, NatureImages, UrbanImages, VermontImages
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

def gallery_abstract(request):
	images = AbstractImages.objects.all()
	logos = WebsiteImage.object.all()
	return render(requst, 'images/abstract.html', {'images': images, 'logos' : logos})

def gallery_nature(request):
	image = NatureImages.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/nature.html', {'images': images, 'logos' : logos})

def gallery_urban(request):
	images = UrbanImages.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/urban.html', {'images': images, 'logos': logos})

def gallery_vermont(request):
	images = VermontImages.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/vermont.html', {'images': images, 'logos': logos})

def gallery(request, gallery_cat):
	if(gallery_cat == "abstract"):
		images = AbstractImages.objects.all()
	elif(gallery_cat == "nature"):
		images = NatureImages.objects.all()
	elif(gallery_cat == "urban"):
		images = UrbanImages.objects.all()		
	elif(gallery_cat == "vermont"):
		images = VermontImages.objects.all()				
	else: images = AbstractImages.objects.all()

	logos = WebsiteImage.objects.all()

	return render(request, 'images/gallery.html', {'images': images, 'logos': logos, 'gallery_cat' : gallery_cat})

def gimage(request, image):
	page_image = GalleryImage.objects.get(name__exact = image)
	logos = WebsiteImage.objects.all()
	return render(request, 'images/image.html', {'image' : page_image, 'logos' : logos})


