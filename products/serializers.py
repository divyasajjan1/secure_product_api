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
            'supplier_cost',
            'internal_notes',
        ]
        read_only_fields = ['supplier_cost', 'internal_notes']