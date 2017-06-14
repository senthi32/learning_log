"""Defines URL patterns for leaarning_logs."""
from django.conf.urls import url
from . import views

urlpatterns = [
	# Home page
	url(r'^$',views.index, name='index'),
	url(r'^topics/$', views.topics, name='topics'),
	#Detail topic pages
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	#All posts -- this is added by me.#
	url(r'^allPost/$', views.all_Post, name='allPost'),
	# Page for adding new topic
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	# Page for adding entry
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	# Page for editting entry
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
	
]
