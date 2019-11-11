from django.db import models
from django.conf import settings



CATEGORY_CHOICES = (
                    ('T' , 'toys'),
                    ('G' , 'gift'),
                    ('E' , 'electric'),
                    ('H' , 'household'),
                    ('F' , 'furniture'),
                    ('S' , 'stationary'),
)

class Item(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    image = models.ImageField(upload_to="items/", null=True, blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="about/", null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    


    def __str__(self):
        return self.name
