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
            'supplier_cost_encrypted',
            'internal_notes_encrypted',
        ]
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get('request')
        
        # Check if user is staff (Admin)
        is_admin = request and request.user.is_authenticated and request.user.is_staff

        if not is_admin:
            # Mask the specific field names used in your model
            ret['supplier_cost_encrypted'] = "********"
            ret['internal_notes_encrypted'] = "Restricted"
        else:
            # OPTIONAL: Decrypt the value so the Admin sees "50" instead of "gAAAA..."
            # This requires importing decrypt_value in your serializer
            from .crypto_utils import decrypt_value
            ret['supplier_cost_encrypted'] = decrypt_value(instance.supplier_cost_encrypted)
            ret['internal_notes_encrypted'] = decrypt_value(instance.internal_notes_encrypted)
            
        return ret