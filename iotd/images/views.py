from django.shortcuts import render_to_response
from images.models import FeaturedImage
from django.conf import settings
from django.http import HttpResponse

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print(settings.STATIC_ROOT)
    return render_to_response('images/home.html',
                              { 'image' : image})
def gallery(request):
	return HttpResponse("Hello, world. You're at the gallery index.")
