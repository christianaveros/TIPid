from django.db import models

# Create your models here.
class Search_bar(models.Model):
	search_term = models.SlugField()

class Item(models.Model):
	# var
	def __str__(self):
		return self.title