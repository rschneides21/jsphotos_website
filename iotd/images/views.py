from django.shortcuts import render_to_response
from images.models import FeaturedImage, GalleryImage
from django.conf import settings
from django.http import HttpResponse

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print(settings.STATIC_ROOT)
    return render_to_response('images/home.html',
                              { 'image' : image})
def gallery(request):
	images = GalleryImage.objects.all()
	# {'images' : image} == key value pair
	return render_to_response('images/gallery.html', {'images' : images})
	
