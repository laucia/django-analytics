from django.test import TestCase
from analytics import analytics, Metric

class RegisterTest(TestCase):
    def test_register(self):
        '''
        Tests basic default behaviour

        '''
        analytics.register('test',Metric(lambda:1+1))

        self.assertEqual(analytics.get()['test'].render(), '2')
        self.assertEqual(analytics.get()['test'].value(), 2)

