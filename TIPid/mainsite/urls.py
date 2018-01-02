from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^search/(?P<search_term>.*)/$', views.SearchView.as_view(), name='search'),
]