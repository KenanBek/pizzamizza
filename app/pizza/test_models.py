from django.test import TestCase
from .models import Pizza, Order


class SimpleTests(TestCase):
    """
    Simple test cases for model classes.
    
    First we setup 2 pizzas and 3 orders.
    Pizzas tested by match of ingredient field.
    Orders tested by match of pizza, size and customer_address.
    """

    def setUp(self):
        hawaiian_pizza = Pizza.objects.create(
            title='HAWAIIAN CHICKEN',
            ingredients='with tomato sauce, chicken meat, pineapples, mozzarella cheese.'
        )
        veggie_pizza = Pizza.objects.create(
            title='VEGGIE LOVER',
            ingredients='with tomato sauce, mushrooms, pineapples, tomatoes, capsicums, onions, mozzarella cheese. '
                        '(Contains garlic, onions and cheese which may not be suitable for vegetarians).'
        )

        Order.objects.create(
            pizza=hawaiian_pizza,
            size=Order.SIZE_30CM,
            customer_name='Kanan',
            customer_address='Tosmur mah.'
        )
        Order.objects.create(
            pizza=veggie_pizza,
            size=Order.SIZE_50CM,
            customer_name='Rita',
            customer_address='Mahmutlar mah.'
        )
        Order.objects.create(
            pizza=hawaiian_pizza,
            size=Order.SIZE_30CM,
            customer_name='David',
            customer_address='Cikceli mah.'
        )

    def test_pizza(self):
        """
        Create 2 pizzas and check for ingedients.
        """

        hawaiian_pizza = Pizza.objects.get(title='HAWAIIAN CHICKEN')
        veggie_pizza = Pizza.objects.get(title='VEGGIE LOVER')

        self.assertEqual(
            hawaiian_pizza.ingredients,
            'with tomato sauce, chicken meat, pineapples, mozzarella cheese.'
        )

        self.assertEqual(
            veggie_pizza.ingredients,
            'with tomato sauce, mushrooms, pineapples, tomatoes, capsicums, onions, mozzarella cheese. '
            '(Contains garlic, onions and cheese which may not be suitable for vegetarians).'
        )

    def test_order(self):
        """
        Create test orders and check for pizza's title, order size and customer address. 
        """

        order_kanan = Order.objects.get(customer_name='Kanan')
        order_rita = Order.objects.get(customer_name='Rita')
        order_david = Order.objects.get(customer_name='David')

        self.assertEqual(
            order_kanan.pizza.title,
            'HAWAIIAN CHICKEN'
        )
        self.assertEqual(
            order_rita.size,
            Order.SIZE_50CM
        )
        self.assertEqual(
            order_david.customer_address,
            'Cikceli mah.'
        )
