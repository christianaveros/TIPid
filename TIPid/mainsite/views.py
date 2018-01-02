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
		context = {
			'history': {
				'title': {'ASS': 0},
				'SSS': {'ASAS': 2}
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

			# packaging
			context = {
				'search_term': request.GET.get('search_term', None),
				'itemlist':{ 'item 1':{'title': 'Who','description': 'What'},'item 2': { 'title': 'Who','description': 'What'}}
			}
		except:
			raise Http404

		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)