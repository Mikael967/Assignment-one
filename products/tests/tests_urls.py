from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import home, products, cart, deleteOrder


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url=reverse('products:home')
        self.assertEqual(resolve(url).func, home)


    def test_cart_url_resolves(self):
        url=reverse('products:cart')
        self.assertEqual(resolve(url).func, cart)

    def test_delete_order_url_resolves(self):
        url=reverse('products:delete_order', args=['some-str'])
        self.assertEqual(resolve(url).func, deleteOrder)


    def test_category_url_resolves(self):
        url=reverse('products:category', args=['some-str'])
        self.assertEqual(resolve(url).func, products)