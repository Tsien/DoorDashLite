# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone_number = models.IntegerField()

    def __unicode__(self):
        return self.user.username


class FoodItem(models.Model):
    name = models.TextField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(default="")
    checkout = models.BooleanField(default=False)
    items = models.ManyToManyField(FoodItem, blank=True, related_name='order', through='OrderItem')

    def __unicode__(self):
        return "Order number: " + repr(self.id)

    def check_out(self):
        if self.checkout:
            raise Exception("It's already checked out!")
        self.checkout = True


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='item')
    quantity = models.IntegerField(default=0)
    instructions = models.TextField(default="")
    subtotal = models.IntegerField(default=0)

