from django.db import models
from django.contrib.auth.models import User
from django.apps import apps 
from django.shortcuts import reverse
from app.utils import GenericComments


class Product(models.Model):
    name = models.CharField(max_length=156)
    price = models.CharField(max_length=25)
    content = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'prod_id': self.id})

class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_name': self.name})


class ProductComent(GenericComments):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)