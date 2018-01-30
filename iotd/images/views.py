from django.shortcuts import render
from images.models import FeaturedImage, GalleryImage
from django.conf import settings
from django.http import HttpResponse
import django_tables2 as tables

# right place for table code?
class ImageTable(tables.Table):
    class Meta:
        model = GalleryImage 

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print(settings.STATIC_ROOT)
    return render(request, 'images/home.html',
                              { 'image' : image})
def gallery(request):
	images = GalleryImage.objects.all()
	image_table = ImageTable(images)
	return render(request, 'images/gallery.html', {"image_table": image_table})

	# {'images' : image} == key value pair, json?
	# return render(request ,'images/gallery.html', {'image' : image})
	
