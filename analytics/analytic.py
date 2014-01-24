from django.template.loader import render_to_string
from django.template import Template, Context

__all__ = ['Analytics','Metric','analytics']

class Analytics(object):
	'''
	Encapsulate a set of registered metrics

	'''
	def __init__(self):
		self._metrics = {}

	def register(self,name, metric):
		'''
		Register a new metric

		'''
		self._metrics[name] = metric

	def get(self):
		'''
		Return the complete list of all registered metrics.

		'''
		return 	self._metrics



class Metric(object):
	'''
	Indicates a value to be computed, and eventually a way to render it

	'''

	def __init__(self, get_result, template="{{ value }}"):
		self.get_result = get_result
		self.template = template if isinstance(template,Template) else Template(template)

	def render(self):
		'''
		Return the result of the given function, with the given template

		'''
		return self.template.render(
				Context({'value':self.get_result()}),
				)
	def value(self):
		'''
		Return the raw current value of the analytic

		'''
		return self.get_result()


# This global object represents the default analytics, for default case.
# You can instantiate Analytics in your own code to create a metric set.
analytics = Analytics()
