from django.test import TestCase, RequestFactory
from CTF.models import *

class RegistrationTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def smoothTest(self):
        request = self.factory.post('/Registration/Register')

        # post for a team form

        # post for passwords

        # post data for all five teammates

        # help link: https://docs.djangoproject.com/en/2.1/topics/testing/advanced/#django.test.RequestFactory
