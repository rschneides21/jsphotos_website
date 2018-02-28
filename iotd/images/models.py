from django.db import models

# Create your models here.

#create abstract base classes for images


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name

    class Meta:
        ordering = ('cat_name',)

class Image(models.Model):
    name       = models.CharField(max_length=200)
    uploaded   = models.DateTimeField(auto_now=True)
    img        = models.ImageField(upload_to="")
    categories = models.ManyToManyField(Category, through = 'Order')

    def __str__(self):
        return self.name

class Order(models.Model):
    image    = models.ForeignKey(Image)
    category = models.ForeignKey(Category)
    order    = models.IntegerField() 






