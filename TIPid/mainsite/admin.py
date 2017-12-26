from django.contrib import admin

from mainsite.models import *

class ItemsModel(admin.ModelAdmin):
    list_display = (
	'id',
	'title',
	'information',
    )
    search_fields = (
	'title',
	'information',
    )


class HistModel(admin.ModelAdmin):
    list_display = (
	'id',
	'history',
	'create_at',
    )

admin.site.register(Item, ItemsModel)
admin.site.register(History, HistModel)


# Register your models here.
