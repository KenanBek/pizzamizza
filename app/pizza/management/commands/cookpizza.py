# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from ...models import Pizza


class Command(BaseCommand):
    """
    Simple command to create meaningful data for tests.
    
    I specially did not use django fixtures or mockups for this test project.
    """

    help = 'Generate test data'

    def handle(self, *args, **options):
        pizza1 = Pizza.objects.create(
            title='BLAZING SEAFOOD',
            ingredients='with spicy sweet sour sauce, tuna, crabsticks, '
                        'pineapples, capsicums, onions, mozzarella cheese.'
        )
        pizza2 = Pizza.objects.create(
            title='CHICKEN SUPREME',
            ingredients='with tomato sauce, chicken meat, chicken salami, '
                        'chicken loaf, mushrooms, capsicums, onions, mozzarella cheese.'
        )
        pizza3 = Pizza.objects.create(
            title='HAWAIIAN SUPREME',
            ingredients='with tomato sauce, chicken meat, chicken loaf, '
                        'pineapples, mozzarella cheese.'
        )
        pizza4 = Pizza.objects.create(
            title='ISLAND SUPREME',
            ingredients='with thousand island sauce, crabsticks, tuna, '
                        'pineapples, onions, mozzarella cheese.'
        )

        self.stdout.write("Yum-yum, it is done!")
