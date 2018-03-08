# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import serializers


class PizzaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pizzas to be viewed or edited.
    
    list:
    list pizzas
    
    retrieve:
    retrieve pizza
    
    create:
    create new pizza
    
    update:
    update exiting pizza
    
    partial_update:
    partially updated existing pizza
    
    delete:
    delete pizza
    """

    queryset = models.Pizza.objects.all().order_by('-id')
    serializer_class = serializers.PizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    
    list:
    list orders with filters
    
    retrieve:
    retrieve order by ID
    
    create:
    create new order
    
    update:
    update exiting order
    
    partial_update:
    partially updated existing order
    
    delete:
    delete order
    """
    queryset = models.Order.objects.all().order_by('-id')
    serializer_class = serializers.OrderSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['status', 'customer_name', ]
    ordering = ['-id', ]
