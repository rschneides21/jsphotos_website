from django.contrib import admin
from images.models import FeaturedImage, GalleryImage, WebsiteImage

# Register your models here.

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'category', 'uploaded')
    ordering = ('-category',)
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"

    thumbnail.allow_tags = True


@admin.register(FeaturedImage)
class FeaturedImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail','name', 'tagline', 'uploaded')
    ordering = ('-uploaded',)
   
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"

    thumbnail.allow_tags = True

@admin.register(WebsiteImage)
class WebsiteImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'uploaded')
    ordering = ('-uploaded',)
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"
    thumbnail.allow_tags = True             


