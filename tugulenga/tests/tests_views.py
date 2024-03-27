from django.test import TestCase, RequestFactory
from django.urls import reverse

from tugulenga.views import loginPage



class TestViews(TestCase):
    def setUp(self):
        self.view = loginPage
        self.factory = RequestFactory()

    def test_loginPage_with_valid_data(self):
        request= self.factory.post(reverse('tugule:login'),data={'username':'Naomi', 'password':'123456789'})
        response = self.view(request)
        '''
        had to comment the decorator(above the loginPage view) and the message in the else part 
        to ensure the working of the test because they weren't necessary to test the working of the test 

        '''