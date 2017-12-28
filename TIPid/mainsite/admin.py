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


admin.site.register(Item, ItemsModel)

# Register your models here.
