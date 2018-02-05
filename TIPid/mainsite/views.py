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
		history_items = Item.objects.all().order_by('-id')

		context = {
			'history_items': history_items
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
			price_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('price')
			rating_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-rating')
			bayes_est_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-bayes_est')
			method = interleaving.TeamDraft([price_ordered_items, rating_ordered_items])
			ranked_ordered_items = method.interleave()

			# plotting
			fig, ax = plt.subplots()

			for index, item in enumerate(ranked_ordered_items):
				if (item.website=='amazon'):
					color = 'red'
				elif (item.website=='lazada'):
					color = 'blue'
				elif (item.website=='shopee'):
					color = 'green'
				
				if index < 10:
					alpha = 1
				else:
					alpha = 0.3
				scatter = ax.scatter(item.price, item.bayes_est, c=color, alpha=alpha, edgecolors='none')
				labels = [str(index+1) + '.) ' + (item.name[0:20] + '...' + '(PHP' + str(item.price) + ')')]
				tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
				mpld3.plugins.connect(fig, tooltip)
			red_patch = mpatches.Patch(color='red', label='Amazon')
			blue_patch = mpatches.Patch(color='blue', label='Lazada')
			green_patch = mpatches.Patch(color='green', label='Shopee')
			ax.legend(handles=[red_patch, blue_patch, green_patch])
			html_graph = mpld3.fig_to_html(fig)


			plt.close()

			# packaging
			context = {
				'search_term': search_term,
				'top_10_result_items': ranked_ordered_items[:10],
				'top_price_result_items': price_ordered_items[:10],
				'top_bayes_est_result_items': bayes_est_ordered_items[:10],
				'figure': html_graph
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
			price_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('price')
			rating_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-rating')
			bayes_est_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-bayes_est')
			method = interleaving.TeamDraft([price_ordered_items, rating_ordered_items])
			ranked_ordered_items = method.interleave()

			# plotting
			fig, ax = plt.subplots()
			for index, item in enumerate(ranked_ordered_items):
				
				if (item.website=='amazon'):
					color = 'red'
				elif (item.website=='lazada'):
					color = 'blue'
				elif (item.website=='shopee'):
					color = 'green'
				
				if index < 10:
					alpha = 1
				else:
					alpha = 0.3
				scatter = ax.scatter(item.price, item.bayes_est, c=color, alpha=alpha, edgecolors='none')
				labels = [str(index+1) + '.) ' + (item.name[0:20] + '...' + '(PHP' + str(item.price) + ')')]
				tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
				mpld3.plugins.connect(fig, tooltip)
			red_patch = mpatches.Patch(color='red', label='Amazon')
			blue_patch = mpatches.Patch(color='blue', label='Lazada')
			green_patch = mpatches.Patch(color='green', label='Shopee')
			ax.legend(handles=[red_patch, blue_patch, green_patch])
			html_graph = mpld3.fig_to_html(fig)


			"""
			chart = dict()
			chart['id'] = "fig_01"
			chart['json'] = json.dumps(mpld3.fig_to_dict(fig))
			result= {'single_chart': single_chart}
			"""

			plt.close()


			#packaging
			context = {
				'search_term': search_term,
				'top_10_result_items': ranked_ordered_items[:10],
				'top_price_result_items': price_ordered_items[:10],
				'top_bayes_est_result_items': bayes_est_ordered_items[:10],
				'figure': html_graph
			}

		except Exception as e:
			raise e

		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)