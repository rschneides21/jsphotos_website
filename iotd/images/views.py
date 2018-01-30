from django.shortcuts import render
from images.models import FeaturedImage, GalleryImage
from django.conf import settings
from django.http import HttpResponse

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print(settings.STATIC_ROOT)
    return render(request, 'images/home.html',
                              { 'image' : image})
def gallery(request):
	images = GalleryImage.objects.all()
	# {'images' : image} == key value pair, json?
	return render(request ,'images/gallery.html', {'images' : images})
	
