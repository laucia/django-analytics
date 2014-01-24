from analytic import *

def autodiscover():
	'''
	Auto-discover INSTALLED_APPS metrics.py modules and fail silently when not
	present. This forces an import on them to register any metric they define.

	'''

	import copy
	from django.conf import settings
	from django.utils.importlib import import_module
	from django.utils.module_loading import module_has_submodule

	for app in settings.INSTALLED_APPS:
		mod = import_module(app)
		# Attempt to import the app's metrics module.
		try:
			before_import_metrics = copy.copy(analytics._metrics)
			import_module('%s.metrics' % app)

		except:
			# Reset the model registry to the state before the last import as
			# this import will have to reoccur on the next request.
			analytics._metrics = before_import_metrics

			# Decide whether to bubble up this error. If the app just
			# doesn't have an metrics.py module, we can ignore the error.
			# Otherwise we want it to bubble up.
			if module_has_submodule(mod, 'metrics'):
				raise

