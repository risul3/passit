from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^\Z', views.index, name="idex")
]