# from django.test import TestCase
# from django.contrib.auth.models import User
# from tugulenga.forms import ProductForm, Business_accountForm, OrderForm, OrderItemForm, CreateUserForm

# class TestForms(TestCase):
#     def test_product_form_valid_data(self):
#         form = ProductForm(data={
#             'image': 'product.jpg',
#             'category': 'electronics',
#             'name': 'Laptop',
#             'price': 1000
#         })

#         self.assertTrue(form.is_valid())

#     def test_product_form_no_data(self):
#         form = ProductForm(data={})

#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 4)

#     def test_business_account_form_valid_data(self):
#         form = Business_accountForm(data={
#             'name': 'mama',
#             'description': 'food'
#         })

#         self.assertTrue(form.is_valid())

#     def test_business_account_form_no_data(self):
#         form = Business_accountForm(data={})

#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 2)

#     def test_order_form_valid_data(self):
#         form = OrderForm(data={
#             'customer': 'Mike',
#             'complete': False
#         })

#         self.assertTrue(form.is_valid())

#     def test_order_form_no_data(self):
#         form = OrderForm(data={})

#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 2)

#     def test_order_item_form_valid_data(self):
#         form = OrderItemForm(data={
#             'product': 'rolex',
#             'quantity': 2
#         })

#         self.assertTrue(form.is_valid())

#     def test_order_item_form_no_data(self):
#         form = OrderItemForm(data={})

#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 2)

#     def test_create_user_form_valid_data(self):
#         form = CreateUserForm(data={
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'password1': 'testpassword123',
#             'password2': 'testpassword123'
#         })

#         self.assertTrue(form.is_valid())

#     def test_create_user_form_no_data(self):
#         form = CreateUserForm(data={})

#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 4)

