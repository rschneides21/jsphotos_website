from django.contrib import admin
from images.models import AbstractImage, NatureImage, UrbanImage, VermontImage, WebsiteImage, FrontPageImage

# Register your models here.

@admin.register(AbstractImage)
class AbstractImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'order', 'category_id', 'uploaded')
    ordering = ('-order',)
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"

    thumbnail.allow_tags = True

@admin.register(NatureImage)
class NatureImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'order', 'category_id','uploaded')
    ordering = ('-order',)
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"

    thumbnail.allow_tags = True

@admin.register(UrbanImage)
class UrbanImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'order', 'category_id', 'uploaded')
    ordering = ('-order',)
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"

    thumbnail.allow_tags = True

@admin.register(VermontImage)
class VermontImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'order', 'category_id', 'uploaded')
    ordering = ('-order',)
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


@admin.register(FrontPageImage)
class FrontPageImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'uploaded')
    ordering = ('-uploaded',)
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"
    thumbnail.allow_tags = True                


