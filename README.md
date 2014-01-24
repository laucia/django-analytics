django-analytics
================

Simple way to have real time indicators about your website
Create per application metrics, in metrics.py files, that 
are loaded and available whenever you need them!

Installation
------------
in ``settings.py``

    INSTALLED_APPS += (
        'analytics',
        )

in your main ``urls.py``

	if 'analytics' in settings.INSTALLED_APPS:
		import analytics
		analytics.autodiscover()

		# Optional only if you want the simple display all page
		urlpatterns += patterns('',
			url (r'^analytics/', include('analytics.urls', namespace = 'analytics')),
		)

Usage & Examples
----------------
Create a ``metrics.py`` file in each application you want to attach metrics to.
This will be loaded automaticaly in a ``django.contrib.admin`` fashion.

sample ``metrics.py``

	from analytics import analytics, Metric

	from django.contrib.auth.models import User

	analytics.register(
		"Number of Users", 
		Metric(User.objects.all().count)
		)

Check code for full documentation

TO DO
-----

+ Write more full proof examples and documentation
+ Write an admin site addon instead of the ugly actual display all page
+ Keep trace of registered indicators through time