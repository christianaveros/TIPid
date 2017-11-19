from django.contrib import admin

from scrapers.models import AmazonProductResponses

class AmazonPR(admin.ModelAdmin):
    list_display = (
	'id',
	'name',
	'response',
    )
    search_fields = (
	'title',
	'note',
    )


admin.site.register(AmazonProductResponses, AmazonPR)

# Register your models here.
