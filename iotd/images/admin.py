from django.contrib import admin
from images.models import Image, Category, Order

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'uploaded', 'get_categories')
    ordering = ('-uploaded',)
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"
    def get_categories(self, obj):
        return "\n".join([c.cat_name for c in obj.categories.all()])

    thumbnail.allow_tags = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    ordering = ('cat_name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('image', 'order', 'category')
    ordering = ('category','order',)

