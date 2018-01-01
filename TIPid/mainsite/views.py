from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponse

class IndexView(CreateView):
	template_name = 'index.html'
	form_class = UserCreationForm
	def search(request):
		if request.method == 'POST':
			#example only
			response_data = {}
			response_data['result'] = 'Create post successful!'
			return JsonResponse(response_data)
		else:
			return JsonResponse({"nothing to see": "this isn't happening"})
		#itemlist = Call a model here that returns a JSON data
		#if (itemlist['data'] == None): 
		#	itemlist['empty'] = True;
		#return JsonResponse(itemlist)
		#content = {
		#	'search': request.GET['search'] if 'search' in request.GET else ''
		#	}
		#return render(request, 'index.html', content)