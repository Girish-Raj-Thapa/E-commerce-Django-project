from rest_framework import serializers

from . models import Category, Product 

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

