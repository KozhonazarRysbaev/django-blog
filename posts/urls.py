from django.conf.urls import url
from django.contrib import admin
from posts import views

urlpatterns = [
	url(r'^$', views.post_home), 
	url(r'^create/$', views.post_create),
	url(r'^read/$', views.post_read),
	url(r'^update/$', views.post_update),
	url(r'^delete/$', views.post_delete),
]