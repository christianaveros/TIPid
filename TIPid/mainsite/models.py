from django.db import models
from django.utils import timezone
from .managers import ItemManager

class Item(models.Model):
	title = models.CharField(max_length=200) # title name of item
	create_at = models.DateTimeField(default=timezone.now(), blank=True)

	objects = ItemManager()

	def __str__(self):
		return self.title

class ScrapedProduct(models.Model):
	
	WEBSITES =(
		('amazon', 'Amazon.com'),
		('lazada', 'Lazada.com.ph'),
		('shopee', 'Shopee.ph')
	)
	
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	name = models.CharField(max_length=512, blank=False)
	website = models.CharField(max_length=32, choices=WEBSITES)
	url = models.URLField()
	price = models.IntegerField(blank=False)
	"""original_price = models.IntegerField()"""
	rating = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
	reviews = models.IntegerField(blank=False)
	bayes_est = models.DecimalField(max_digits=10, decimal_places=10, blank=False)

	def __str__(self):
		return self.title

class Sample(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	name = models.CharField(max_length=512, blank=False)

	def __str__(self):
		return self.name	


"""

class ScrapedAmazonProducts(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=512, blank=False)
	url = models.URLField()
    price = models.IntegerField(blank=False)
	original_price = models.IntegerField()
	rating = models.DecimalField(blank=False)
	reviews = models.IntegerField(blank=False)
	bayes_est = models.DecimalField(blank=False)
    def __str__(self):
        return self.title

class ScrapedLazadaProducts(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=512, blank=False)
    price = models.IntegerField(blank=False)
	original_price = models.IntegerField()
	rating = models.DecimalField(blank=False)
	reviews = models.IntegerField(blank=False)
	bayes_est = models.DecimalField(blank=False)
    def __str__(self):
        return self.title

class ScrapedShopeeProducts(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=512, blank=False)
    price = models.IntegerField(blank=False)
	original_price = models.IntegerField()
	rating = models.DecimalField(blank=False)
	reviews = models.IntegerField(blank=False)
	bayes_est = models.DecimalField(blank=False)

    def __str__(self):
        return self.title

class RankedProductList(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	name = models.CharField(max_length=512, blank=False)
    price = models.IntegerField(blank=False)
	original_price = models.IntegerField()
	rating = models.DecimalField(blank=False)
	reviews = models.IntegerField(blank=False)
	bayes_est = models.DecimalField(blank=False)

    def __str__(self):
        return self.title

"""
