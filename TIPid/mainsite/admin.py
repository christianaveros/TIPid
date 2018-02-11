from django.contrib import admin

from mainsite.models import *

class ItemsModel(admin.ModelAdmin):
	list_display = (
	'id',
	'title',
	'create_at',
	)
	search_fields = (
	'title',
	)


class ScrapedProductModel(admin.ModelAdmin):
	list_display = (
	'id',
	'item',
	'name',
	'website',
	'url',
	'price',
	'rating',
	'reviews',
	'bayes_est',
	'ranking',
	'imageurl'
	)
	search_fields = (
	'item',
	'name',
	'website'
	)

admin.site.register(Item, ItemsModel)
admin.site.register(ScrapedProduct, ScrapedProductModel)

# Register your models here.
