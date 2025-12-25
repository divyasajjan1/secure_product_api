from django.db import models
from encrypted_model_fields.fields import EncryptedCharField, EncryptedTextField, EncryptedIntegerField

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=10, unique=True)
    product_category = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_manufacturing_date = models.DateField()
    product_expiry_date = models.DateField()

    # Encrypted fields
    supplier_cost = EncryptedIntegerField(null=True, blank=True)
    internal_notes = EncryptedTextField(null=True, blank=True)

    def __str__(self):
        return self.product_id
