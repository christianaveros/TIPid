from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class IndexView(CreateView):
	template_name = 'index.html'
	form_class = UserCreationForm

def search(request):
	search = request.GET.get('search', None)
	#itemlist = Call a model here that returns a JSON data
	if (itemlist['data'] == None): 
		itemlist['empty'] = True;
	return JsonResponse(itemlist)
	#content = {
	#	'search': request.GET['search'] if 'search' in request.GET else ''
	#	}
	#return render(request, 'index.html', content)