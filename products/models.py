# products/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='products')
    # Optional: for featured products on the homepage
    is_featured = models.BooleanField(default=False)

    def _str_(self):
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    artist = models.ForeignKey(Artist, on_delete=models.SET_DEFAULT, default=1)  # Default artist
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)  # For homepage feature

    def _str_(self):
        return self.name