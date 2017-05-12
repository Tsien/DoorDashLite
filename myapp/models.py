# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone_number = models.IntegerField()

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

'''
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, phone_number=kwargs['phone_number'])

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()
'''


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
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_cart')
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='items')

    def __unicode__(self):
        return repr(self.item)



