from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tugulenga.views import home, signup, loginPage, add_product#, add_business_account,add_orderItem

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:home')
        self.assertEqual(resolve(url).func, home)
        #print(resolve(url))# to be able to see the expected view function

    def test_signup_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:signup')
        self.assertEqual(resolve(url).func, signup)

    def test_login_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:login')
        self.assertEqual(resolve(url).func, loginPage)

    def test_add_product_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:add_product')
        self.assertEqual(resolve(url).func, add_product)

    # def test_add_business_account_url_is_resolved(self): #testing if the url calls the right view function
    #     url=reverse('tugule:add_business_account')
    #     self.assertEqual(resolve(url).func, add_business_account)

    # def test_add_orderItem_url_is_resolved(self): #testing if the url calls the right view function
    #     url=reverse('tugule:add_orderItem')
    #     self.assertEqual(resolve(url).func, add_orderItem )