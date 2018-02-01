from django.shortcuts import render
from images.models import FeaturedImage, GalleryImage, WebsiteImage, FrontPageImage
from django.conf import settings
from django.http import HttpResponse

def home(request):
    logo = WebsiteImage.objects.get(name = 'Logo')
    images = FrontPageImage.objects.all() 
    print(settings.STATIC_ROOT)
    return render(request, 'images/home.html',
                              { 'logo' : logo, 'images' : images})
def gallery(request):
	images = GalleryImage.objects.all()
	# {'images' : image} == key value pair, json?
	return render(request ,'images/gallery.html', {'images' : images})
	
