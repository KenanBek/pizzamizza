# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Pizza(models.Model):
    """
    Pizza model used in order for pickup list.
    """

    title = models.CharField(max_length=255)  # Title of the Pizza (eg. Blazing seafood, hawaiian chicken, etc.)
    ingredients = models.CharField(max_length=255)  # What is made of (eg. 'with tomato, sauce, chicken meat, etc.)

    def __unicode__(self):
        return self.title


class Order(models.Model):
    """
    Main order model. Contains FK to Pizza model.
    
    Manually added following indexes: 
    """

    # Status of the order: Order received, preparing order, cooking, on the way, closed
    # Taken from https://www.pizzahut.com.my/en/order/status :)
    STATUS_RECEIVED = 1  # We got the order waiting for processing
    STATUS_PREPARING = 2  # Processing order: collection ingredients, getting chef ready, ...
    STATUS_COOKING = 3  # Yum-yum, it is cooking
    STATUS_ON_THE_WAY = 4  # Delivery man on the way
    STATUS_CLOSED = 5  # Customer is happy and order is closed (maybe som feedback? hmm...)
    STATUS_CHOICES = (
        (STATUS_RECEIVED, 'Received'),
        (STATUS_PREPARING, 'Preparing'),
        (STATUS_COOKING, 'Cooking'),
        (STATUS_ON_THE_WAY, 'On the way'),
        (STATUS_CLOSED, 'Closed'),
    )

    # As a value I will use real centimeters instead of 1, 2, 3
    # it is more human readable (even if it is in DB)
    # in future we can add more sizes without confusion (like SIZE_40CM=3)
    SIZE_30CM = 30
    SIZE_50CM = 50
    SIZE_CHOICES = (
        (SIZE_30CM, '30 Centimeters'),
        (SIZE_50CM, '50 Centimeters'),
    )

    added_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)  # Auto set add time
    modified_at = models.DateTimeField(auto_now=True, editable=False, null=True)  # Auto set/update last modify time

    status = models.PositiveSmallIntegerField(  # Status of the order
        choices=STATUS_CHOICES,
        default=STATUS_RECEIVED,
        db_index=True,  # In case if we want to filter by status of all orders (eg. 'Orders on the way')
    )
    pizza = models.ForeignKey(Pizza)  # Pizza from pre-entered list
    size = models.PositiveSmallIntegerField(choices=SIZE_CHOICES)  # Size of the ordered pizza
    customer_name = models.CharField(max_length=255, db_index=True)  # Name of the customer
    customer_address = models.CharField(max_length=255)  # Address of the customer

    def __unicode__(self):
        return 'Order #{}: {} {} ({})'.format(  # eg. 'Order #101: African Crocodile 50CM (On the way)'
            self.id,
            self.pizza,
            self.get_size_display(),
            self.get_status_display()
        )
