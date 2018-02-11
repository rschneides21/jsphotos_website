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
	
def image(request, image):
	image_obj = GalleryImage.objects.get(id = image)
	logos = WebsiteImage.objects.all()
	return render(request, 'images/image.html', {'image' : image_obj, 'logos' : logos})

def about(request):
	images = GalleryImage.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/about.html', {'images' : images, 'logos' : logos})

def aimage(request, image_id):
	image = get_object_or_404(GalleryImage, pk = image_id)
	images = GalleryImage.objects.all()
	logos = WebsiteImage.objects.all()
	return render(request, 'images/image.html', {'images' : images, 'logos' : logos})	