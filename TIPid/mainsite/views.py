from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import Http404, HttpResponse, JsonResponse
from mainsite.tasks import *
from django.shortcuts import render

class IndexView(CreateView):
	template_name = 'index.html'
	form_class = UserCreationForm

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

"""
def search(request):
	
	if request.method == 'POST':
		#example only
		response_data = {}
		response_data['result'] = 'Create post successful!'
		return JsonResponse(response_data)
	else:
		return JsonResponse({"nothing to see": "this isn't happening"})
	
	search_term = request.GET.get('search', None)
	return JsonResponse({'search_term': search_term})
	#itemlist = Call a model here that returns a JSON data
	#if (itemlist['data'] == None): 
	#	itemlist['empty'] = True;
	#return JsonResponse(itemlist)
	#content = {
	#	'search': request.GET['search'] if 'search' in request.GET else ''
	#	}
	#return render(request, 'index.html', content)

"""