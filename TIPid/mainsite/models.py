from django.db import models
from django.utils import timezone

class History(models.Model):
	history = models.CharField(max_length=200)
	create_at = models.DateTimeField(default=timezone.now(), blank=True)
	def __str__(self):
		return self.history


class Item(models.Model):
	title = models.CharField(max_length=200) # title name of item
	information = models.TextField() # links. info. specs.
	def __str__(self):
		return self.title
