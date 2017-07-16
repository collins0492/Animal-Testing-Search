from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from search.models import Tester
import search.utils

urlpatterns = [
	url(r'^$', views.index, name="index"),
	#url(r'^$', ListView.as_view(queryset=Tester.objects.all().order_by("company"), template_name="search/home.html")),
	url(r'^renewdb$', views.renewdb, name="renewdb"),
	#url(r'^renewdb$', search.utils.renewdb, name='renewdb'),
]