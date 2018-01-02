#from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import Http404, HttpResponse, JsonResponse
from mainsite.tasks import *
from django.shortcuts import render

class IndexView(CreateView):
	template_name = 'index.html'
	#form_class = UserCreationForm

	def get(self, request, *args, **kwargs):
		#preset. run an DB query for history
		context = {
			'history': {
				'Blue ring': {'ASS': 0},
				'Apple iPhone 6s': {'ASAS': 2}
			}
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
			# top_list = [{'rank': 1, 'title': 'wtf', 'description': 'wtf, bro', 'link': 'wtf.com'}, ...]

			# packaging
			context = {
				'search_term': request.GET.get('search_term', None),
				'toprank_itemlist': [{'title': 'Who','description': 'What'},{ 'title': 'Who','description': 'What'}],
				'lazada_itemlist': [{'title': 'lazada title 1','description': 'lazada desc 1'},{ 'title': 'lazada title 2','description': 'lazada desc 2'}]
			}
		except:
			raise Http404

		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)