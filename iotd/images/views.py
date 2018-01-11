from django.shortcuts import render_to_response
from images.models import FeaturedImage
from django.conf import settings

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print(settings.STATIC_ROOT)
    return render_to_response('images/home.html',
                              { 'image' : image})
#TC 3
def images(request):
	return HttpResponse("Hello, world. You're at the images index.")
