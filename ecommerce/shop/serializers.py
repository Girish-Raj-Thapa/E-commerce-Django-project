from rest_framework import serializers
from . models import Category, Product, Cart, Order, OrderProduct 

# Serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta: 
        model = Product 
        fields = ['id', 'title', 'description', 'price', 'stock', 'category', 'category_id']


class CartHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']

class CartSerializer(serializers.ModelSerializer):
    product = CartHelpSerializer()

    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity', 'price']

    
class CartAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'quantity']
        extra_kwargs = {
            'quantity': {'min_value': 1}
        }

class CartRemoveSerializer(serializers.ModelSerializer):
    pass 


