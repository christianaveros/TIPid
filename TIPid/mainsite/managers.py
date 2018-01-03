from django.db import models

class ItemManager(models.Manager):
	def create_item(self, title, item_list):
		item = self.create(title=title)
		from mainsite.models import Sample, ScrapedProduct
		for product in item_list:
			ScrapedProduct.objects.create(item=item, **product)
		
		return item


