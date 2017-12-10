from django.shortcuts import render
from .models import Search_bar

# Create your views here.
def index(request):
	if(request.method == 'POST'):
		content = {
			'int': request.POST['int']
		}
	else:
		content = {
			'int': '0'
		}
	return render(request, 'index.html', content)