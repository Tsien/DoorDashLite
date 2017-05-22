from rest_framework import serializers
from .models import Customer, FoodItem, Order, OrderItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(source='customer.phone_number')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        customer = validated_data.pop('customer', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        customer = Customer(user=instance, **customer)
        customer.save()

        return instance

    def update(self, instance, validated_data):
        customer = validated_data.pop('customer', None)
        Customer.objects.update_or_create(user=instance, defaults=customer)
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'quantity', 'instructions', 'subtotal', 'order', 'item')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='order', many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'address', 'checkout', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('orderitem', None)
        instance = self.Meta.model(**validated_data)
        OrderItem.objects.update_or_create(order=instance, defaults=items_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        items_data = validated_data.pop('orderitem', None)
        OrderItem.objects.update_or_create(order=instance, defaults=items_data)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
