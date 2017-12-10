from django.shortcuts import render
from .models import Search_bar

# Create your views here.
def index(request):
	content = {
		'id': 0
	}
	return render(request, 'index.html', content)