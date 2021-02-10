from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File
from django.utils.text import slugify
from django.urls import reverse

from vendor.models import Vendor


class Category(models.Model):
    title = models.CharField(max_length=254)
    category_slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['title',]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.title, allow_unicode=True)
        return super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)

    title = models.CharField(max_length=254)
    product_slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='products/thumbs/', blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.title, allow_unicode=True)
        return super(Product, self).save(*args, **kwargs)

    def make_thumb(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def get_thumb(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumb(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jgp'

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={
            'pk': self.pk,
            'category_slug': self.category.category_slug,
            'product_slug': self.product_slug
        })
    
