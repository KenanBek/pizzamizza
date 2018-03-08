# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


@admin.register(models.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    """
    Display standard fields of Pizza model.
    """
    pass


@admin.register(models.Order)
class CartAdmin(admin.ModelAdmin):
    """
    Display informative fields of Cart model with ability to filter by status, size and date/times.
    """

    # Filter by status and size fields
    list_filter = ['status', 'size', 'added_at', 'modified_at', ]

    # Display order fields
    list_display = [
        'pizza', 'size',
        'customer_name', 'customer_address', 'status',
        'modified_at'
    ]
