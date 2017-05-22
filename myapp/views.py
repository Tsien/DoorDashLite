# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import FoodItem, Order, OrderItem
from serializers import UserSerializer, FoodItemSerializer, OrderSerializer, OrderItemSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets, status

from rest_framework.views import APIView

from django.contrib.auth.models import User
from rest_framework import permissions
from permission import IsOwner
from django.http import Http404
import sys


# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list', request=request, format=format),
        'food': reverse('item_list', request=request, format=format),
        'order': reverse('order_list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
    })


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class ItemList(APIView):
    '''
    List all items
    '''

    def get(self, request, format=None):
        minx = request.GET.get('min', None)
        maxx = request.GET.get('max', None)
        print min, ", ", max
        if minx is None or maxx is None:
            items = FoodItem.objects.all()
        else:
            items = FoodItem.objects.filter(price__lt=maxx).filter(price__gt=minx)
        serializer = FoodItemSerializer(items, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrderDetail(APIView):
    '''
    Retrieve, update or delete an order
    '''

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class AddItemView(APIView):
    '''
    Add item to an order
    '''

    def post(self, request, pk, format=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
