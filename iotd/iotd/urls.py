from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import images.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', images.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
