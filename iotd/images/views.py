from django.shortcuts import render
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
	# {'images' : image} == key value pair, json?
	return render(request ,'images/gallery.html', {'images' : images, 'logos' : logos})

def about(request):
	images = GalleryImage.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/about.html', {'images' : images, 'logos' : logos})

def aimage(request, image):
	page_image = get_object_or_404(GalleryImage, pk = image)
	logos = WebsiteImage.objects.all()
	return render(request, 'images/image.html', {'image' : page_image, 'logos' : logos})

def image(request, image):
	image_obj = get_object_or_404(GalleryImage, pk = slug)
	logos = WebsiteImage.objects.all()
	return render(request, 'images/image.html', {'image' : image_obj, 'logos' : logos})
