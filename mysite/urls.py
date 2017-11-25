"""
	MYSITE app urls
"""

from django.conf.urls import url

from . import views

app_name = 'mysite'
urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^post/save/$', views.save, name='save'),
	url(r'^post/(?P<slug>[-\w]+)/$', views.show, name='show'),
	# url(r'^(?P<slug>[a-zA-Z]+)/$', views.show, name='show'),
]