# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone_number = models.IntegerField()
    is_blacklisted = models.BooleanField(default=False)
    num_orders = models.IntegerField(default=0)

    def blacklist(self):
        if self.is_blacklisted:
            raise Exception("Already in blacklist!")
        self.is_blacklisted = True

    def __unicode__(self):
        return self.user.username


class FoodItem(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    num_added = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def deactivate(self):
        if not self.is_active:
            raise Exception("Already deactivated!")
        self.is_active = False

    def __unicode__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(default="")
    checkout = models.BooleanField(default=False)
    items = models.ManyToManyField(FoodItem, blank=True, related_name='order', through='OrderItem')
    deliver_fee = models.IntegerField(default=0)
    is_delivered = models.BooleanField(default=False)

    def __unicode__(self):
        return "Order number: " + repr(self.id)

    def check_out(self):
        if self.checkout:
            raise Exception("It's already checked out!")
        self.checkout = True

    def modify_fee(self, fee):
        self.deliver_fee = fee

    def deliver(self):
        if self.is_delivered:
            raise Exception("Already delivered!")
        self.is_delivered = True

    def revert_delivery(self):
        if not self.is_delivered:
            raise Exception("It's not delivered!")
        self.is_delivered = False


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='item')
    quantity = models.IntegerField(default=0)
    instructions = models.TextField(default="")
    subtotal = models.IntegerField(default=0)

