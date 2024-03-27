from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tugulenga.views import home, signup, loginPage, add_product#, add_business_account,add_orderItem

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:home')
        self.assertEquals(resolve(url).func, home)
        #print(resolve(url))# to be able to see the expected view function

    def test_signup_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:signup')
        self.assertEquals(resolve(url).func, signup)

    def test_login_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_add_product_url_is_resolved(self): #testing if the url calls the right view function
        url=reverse('tugule:add_product')
        self.assertEquals(resolve(url).func, add_product)

    # def test_add_business_account_url_is_resolved(self): #testing if the url calls the right view function
    #     url=reverse('tugule:add_business_account')
    #     self.assertEquals(resolve(url).func, add_business_account)

    # def test_add_orderItem_url_is_resolved(self): #testing if the url calls the right view function
    #     url=reverse('tugule:add_orderItem')
    #     self.assertEquals(resolve(url).func, add_orderItem )