from django.shortcuts import render, get_object_or_404, redirect
from images.models import Image, Category
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    logos = Image.objects.filter(categories__cat_name = 'logo').order_by('order__order')
    images = Image.objects.filter(categories__cat_name = 'front_page').order_by('order__order')
    print(settings.STATIC_ROOT)
    return render(request, 'images/home.html',
                              { 'logos' : logos, 'images' : images})
def about(request):
	return render(request, 'images/about.html', {'images' : images, 'logos' : logos})    


def gallery(request, gallery_cat):
	images = Image.objects.filter(categories__cat_name = gallery_cat)
	logos =  Image.objects.filter(categories__cat_name = 'logo')

	return render(request, 'images/gallery.html', {'images': images, 'logos': logos, 'gallery_cat' : gallery_cat})

def gimage(request, image_cat, image):
	page_image = Image.objects.get(name__exact = image)			
	logos = Image.objects.filter(categories__cat_name = 'logo')
	return render(request, 'images/image.html', {'image' : page_image, 'logos' : logos})


