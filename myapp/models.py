# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    phone_number = models.IntegerField()

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class FoodItem(models.Model):
    name = models.TextField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(default="")
    checkout = models.BooleanField(default=False)

    def __unicode__(self):
        return "Order number: " + repr(self.id)

class Order_Items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    def __unicode__(self):
        return repr(self.item)



