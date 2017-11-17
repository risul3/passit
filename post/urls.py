from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^\Z', views.index, name='index'),
	url(r'^(?P<slug>[a-zA-Z]+)/$', views.show, name='show'),
]