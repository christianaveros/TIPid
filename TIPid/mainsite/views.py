from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import Http404, HttpResponse, JsonResponse
from mainsite.tasks import *
from django.shortcuts import render
from mainsite.models import ScrapedProduct, Item
import interleaving

class IndexView(CreateView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		history_items = Item.objects.all().order_by('-create_at')

		context = {
			'history_items': history_items
		}
		return render(request, self.template_name, context)

class SearchView(View):
	template_name = 'search.html'

	def get_context_data(self, request):
		context = {}
		try:
			# run APIs here
			#lazada_itemlist = scraper_lazada.add_async(request.GET.get('search_term', None)).get()

			# run ranking here. 1 - 10
			# top_rank_list = [{'rank': 1, 'title': 'wtf', 'description': 'wtf, bro', 'link': 'wtf.com'}, ...]

			# packaging
			context = {
				'search_term': request.GET.get('search_term', None),
				'top_rank_items': [{'name': 'Who','description': 'What'},{ 'name': 'Who','description': 'What'}],
				'lazada_items': [{'name': 'lazada title 1','description': 'lazada desc 1'},{ 'name': 'lazada title 2','description': 'lazada desc 2'}]
			}
		except:
			raise Http404

		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)

class HistoryView(View):
	template_name = 'history.html'

	def get_context_data(self, request):
		context = {}
		try:
			#db query
			item_id = request.GET.get('id', None)
			search_term = request.GET.get('search_term', None)

			#top rank
			price_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('price')
			rating_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-rating')
			bayes_est_ordered_items = ScrapedProduct.objects.filter(item=Item.objects.filter(id=item_id)).order_by('-bayes_est')
			method = interleaving.TeamDraft([price_ordered_items, rating_ordered_items])
			ranked_ordered_items = method.interleave()

			#packaging
			context = {
				'search_term': search_term,
				'top_10_result_items': sorted(ranked_ordered_items[:10], key=lambda Item: Item.bayes_est, reverse=True),
				'top_price_result_items': price_ordered_items[:10],
				'top_bayes_est_result_items': bayes_est_ordered_items[:10]
			}
		except:
			raise Http404

		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)