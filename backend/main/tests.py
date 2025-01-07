from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class ProductTests(APITestCase):
    def test_create_product(self):
        url = reverse('add_product')
        data = {'name': 'Product 1', 'description': 'Description of product', 'price': 10.99, 'stock': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

from django.test import TestCase
from main.models import Product

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name="Sample Product", price=100.0)
        self.assertEqual(product.name, "Sample Product")
