from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import create_order_item, home, products, cart, deleteOrder


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url=reverse('products:home')
        self.assertEquals(resolve(url).func, home)

    def test_order_url_resolves(self):
        url=reverse('products:order', args=['some-str'])
        self.assertEquals(resolve(url).func, create_order_item)

    def test_cart_url_resolves(self):
        url=reverse('products:cart')
        self.assertEquals(resolve(url).func, cart)

    def test_delete_order_url_resolves(self):
        url=reverse('products:delete_order', args=['some-str'])
        self.assertEquals(resolve(url).func, deleteOrder)


    def test_category_url_resolves(self):
        url=reverse('products:category', args=['some-str'])
        self.assertEquals(resolve(url).func, products)