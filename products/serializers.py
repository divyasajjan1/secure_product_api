from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'product_id',
            'product_category',
            'product_price',
            'product_manufacturing_date',
            'product_expiry_date',
        ]
        