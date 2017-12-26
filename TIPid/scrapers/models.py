from __future__ import unicode_literals

from django.db import models
"""
class AmazonScrapedProducts(models.Model):
    name = models.CharField(max_length=512, blank=False)
    response = models.TextField(blank=False)

    def __str__(self):
        return self.title

class LazadaScrapedProducts(models.Model):
    name = models.CharField(max_length=512, blank=False)
    price = models.IntegerField(blank=False)
	discount = models.CharField(max_length=512, blank=False)
	original_price = models.IntegerField(blank=False)
	rating = models.DecimalField(blank=False)
	reviews = models.IntegerField(blank=False)
    def __str__(self):
        return self.title

class ShopeeScrapedProducts(models.Model):
	# search_item = ForeignKey()
    name = models.CharField(max_length=512, blank=False)
    price = models.IntegerField(blank=False)
	discount = models.CharField(max_length=512, blank=False)
	original_price = models.IntegerField(blank=False)
	rating = models.DecimalField(blank=False)
	reviews = models.IntegerField(blank=False)

    def __str__(self):
        return self.title

"""
# Create your models here.
