from rest_framework import serializers
from .models import Customer, FoodItem, Order, Order_Items
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
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        customer = Customer(user=instance, **customer)
        instance.save()
        return instance

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_cart = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id', 'customer', 'address', 'checkout', 'order_cart')
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
