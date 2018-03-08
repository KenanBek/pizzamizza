# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from . import models


class PizzaSerializer(serializers.ModelSerializer):
    """
    Model serializer for Pizza.
    """

    class Meta:
        model = models.Pizza
        fields = ('title', 'ingredients')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked model serializer for Order model with link to Pizza details.
    """

    class Meta:
        model = models.Order
        fields = ('id', 'status', 'pizza', 'size', 'customer_name', 'customer_address')
