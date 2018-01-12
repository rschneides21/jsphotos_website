from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import images.views

#eventually have images path be image category pulled from database
urlpatterns = [
	#try changing include(admin.site.urls) -> admin.site.urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^$', images.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
