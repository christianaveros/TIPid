from django.db import models

class ItemManager(models.Manager):
	def create_item(self, title):
		item = self.create(title=title)
		from mainsite.models import Sample
		sample = Sample.objects.create(item=item, name='what')		

		return item, sample


