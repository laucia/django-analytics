from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	# Project Management
	url(r'^$', 'analytics.views.show_analytics', name ='index'),
	)