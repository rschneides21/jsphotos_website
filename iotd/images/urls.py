#TC2 all

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
]