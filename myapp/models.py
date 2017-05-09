# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	email = models.TextField()
	phone_number = models.IntegerField()

class FoodItem(models.Model):
	name = models.TextField()
	price = models.IntegerField()

	def __unicode__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order_Items(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

class Author(models.Model):
	name = models.TextField(blank=True, null=True)
  
class Book(models.Model):
	name = models.TextField(blank=True, null=True)
	author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	sale_price = models.IntegerField(default=0)
	production_cost = models.IntegerField(default=0)
  
class Consumer(models.Model):
	first_name = models.TextField(blank=True, null=True)
	last_name = models.TextField(blank=True, null=True)
	books = models.ManyToManyField(Book)