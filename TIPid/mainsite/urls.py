from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^search/', views.SearchView.as_view(), name='search'),
	url(r'^history/', views.HistoryView.as_view(), name='history'),
]