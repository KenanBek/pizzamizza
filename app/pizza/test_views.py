from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pizza, Order


class SimpleAPITests(APITestCase):
    """
    Simple API test cases for create, list, update and delete endpoints.
    """

    def setUp(self):
        veggie_pizza = Pizza.objects.create(
            title='VEGGIE LOVER',
            ingredients='with tomato sauce, mushrooms, pineapples, tomatoes, capsicums, onions, mozzarella cheese. '
                        '(Contains garlic, onions and cheese which may not be suitable for vegetarians).'
        )
        Order.objects.create(
            pizza=veggie_pizza,
            size=Order.SIZE_50CM,
            customer_name='Rita',
            customer_address='Mahmutlar mah.'
        )

    def test_get_pizza(self):
        """
        Check that we can create pizza.
        """

        pizza_url = reverse('pizza-detail', kwargs={'pk': 1})
        pizza_response = self.client.get(pizza_url)
        self.assertEqual(pizza_response.status_code, status.HTTP_200_OK)
        self.assertEqual(pizza_response.data['title'], 'VEGGIE LOVER', 'Can not properly get pizza')

    def test_create_order(self):
        """
        Post new order and check by total order counts. 
        """

        order_url = reverse('order-list')
        order_data = {
            'pizza': reverse('pizza-detail', kwargs={'pk': 1}),  # because of HyperlinkedModelSerializer
            'size': Order.SIZE_30CM,
            'customer_name': 'Kanan',
            'customer_address': 'Baku, Azerbaijan'
        }
        order_response = self.client.post(order_url, order_data)
        self.assertEqual(order_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    def test_filter_order(self):
        """
        Call order list with customer_name filter.
        Checked by setup data.
        """

        order_url = reverse('order-list')
        order_data = {
            'customer_name': 'Rita',
        }
        order_response = self.client.get(order_url, order_data)
        self.assertEqual(order_response.status_code, status.HTTP_200_OK)
        self.assertEqual(order_response.data['results'][0]['customer_name'], 'Rita')
        self.assertEqual(order_response.data['results'][0]['size'], 50)
