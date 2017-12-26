from django.shortcuts import render

def index(request):
	content = {
		'search': request.GET['search'] if 'search' in request.GET else ''
		}
	return render(request, 'index.html', content)