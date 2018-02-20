from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import images.views

#eventually have images path be image category pulled from database
urlpatterns = [
	#try changing include(admin.site.urls) -> admin.site.urls
    url(r'^admin/', include(admin.site.urls)),
    #TC1 added images path, not sure about 'images.urls'
    url(r'^gallery/', include('images.urls')),
    url(r'^about/', images.views.about, name = 'about'),
    url(r'^(?P<gallery_cat>[-\w]+)/$', images.views.gallery, name = 'gallery'),
    url(r'^(?P<image_cat>[-\w]+)/(?P<image>[-\w]+)/$', images.views.gimage, name = 'gallery_image'),
    url(r'^$', images.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
