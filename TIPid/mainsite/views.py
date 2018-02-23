# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import Http404, HttpResponse, JsonResponse
from mainsite.tasks import *
from django.shortcuts import render
from mainsite.models import ScrapedProduct, Item
import interleaving
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import mpld3
import numpy as np
import json

class IndexView(CreateView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		history_items = Item.objects.all().order_by('-id')[0:5]
		products = []
		for history_item in history_items:
			products.append({'history_item': history_item, 'products': ScrapedProduct.objects.filter(item=history_item).order_by('ranking')[0:5]})


		context = {
			'history_items': products,

		}
		return render(request, self.template_name, context)

class SearchView(View):
	template_name = 'search.html'

	def get_context_data(self, request):
		context = {}
		try:
			# scraping
			search_term = request.GET.get('search_term', None)
			item_id = scrapers(search_term)
			price_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id), bayes_est__gte=4).order_by('price')
			rating_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-rating')
			bayes_est_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-bayes_est')
			method = interleaving.TeamDraft([price_ordered_items, rating_ordered_items])
			ranked_ordered_items = method.interleave()
			ranked_ordered_items = sorted(ranked_ordered_items, key=lambda Item: Item.bayes_est, reverse=True)

			for index, item in enumerate(ranked_ordered_items):
				item.ranking = index
				item.save(update_fields=['ranking'])

			# packaging
			context = {
				'search_term': search_term,
				'top_10_result_items': ranked_ordered_items[:10],
				'top_price_result_items': price_ordered_items[:10],
				'top_bayes_est_result_items': bayes_est_ordered_items[:10],
			}
		except Exception as e:
			raise e

		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)

class HistoryView(View):
	template_name = 'history.html'

	def get_context_data(self, request):
		context = {}
		try:
			# db query
			item_id = request.GET.get('id', None)
			search_term = request.GET.get('search_term', None)

			# top rank
			price_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id), bayes_est__gte=4).order_by('price')
			rating_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-rating')
			bayes_est_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-bayes_est')
			method = interleaving.TeamDraft([price_ordered_items, rating_ordered_items])
			ranked_ordered_items = method.interleave()
			ranked_ordered_items = sorted(ranked_ordered_items, key=lambda Item: Item.bayes_est, reverse=True)

			for index, item in enumerate(ranked_ordered_items):
				item.ranking = index
				item.save(update_fields=['ranking'])

			#packaging
			context = {
				'search_term': search_term,
				'top_10_result_items': sorted(ranked_ordered_items[:10], key=lambda Item: Item.bayes_est, reverse=True),
				'top_price_result_items': price_ordered_items[:10],
				'top_bayes_est_result_items': bayes_est_ordered_items[:10],
			}

		except Exception as e:
			raise e

		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)