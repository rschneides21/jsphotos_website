from django.shortcuts import render, get_object_or_404
from images.models import FeaturedImage, GalleryImage, WebsiteImage, FrontPageImage
from django.conf import settings
from django.http import HttpResponse

def home(request):
    logos = WebsiteImage.objects.all()
    images = FrontPageImage.objects.all() 
    print(settings.STATIC_ROOT)
    return render(request, 'images/home.html',
                              { 'logos' : logos, 'images' : images})
def gallery(request):
	images = GalleryImage.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request ,'images/gallery.html', {'images' : images, 'logos' : logos})

def about(request):
	images = GalleryImage.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/about.html', {'images' : images, 'logos' : logos})

def gimage(request, image):
	page_image = GalleryImage.objects.get(name__exact = image)
	logos = WebsiteImage.objects.all()
	return render(request, 'images/image.html', {'image' : page_image, 'logos' : logos})


