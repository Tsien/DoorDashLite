# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Customer, FoodItem, Order, Order_Items
from serializers import UserSerializer, FoodItemSerializer, OrderSerializer, OrderItemSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from rest_framework import permissions
from permission import IsOwner
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'food': reverse('item-list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
        'order': reverse('order-list', request=request, format=format),
        })

class CustomerList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FoodItemList(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner, )

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OrderItemList(generics.ListCreateAPIView):
    queryset = Order_Items.objects.all()
    serializer_class = OrderItemSerializer

class RegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
