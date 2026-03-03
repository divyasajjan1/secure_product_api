from django.db import models
#from encrypted_model_fields.fields import EncryptedTextField, EncryptedIntegerField
from .crypto_utils import encrypt_value, decrypt_value

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=10, unique=True)
    product_category = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_manufacturing_date = models.DateField()
    product_expiry_date = models.DateField()

    # Encrypted fields
    # supplier_cost = EncryptedIntegerField(null=True, blank=True)
    # internal_notes = EncryptedTextField(null=True, blank=True)

    # We store the ENCRYPTED string in these standard fields
    supplier_cost_encrypted = models.TextField(null=True, blank=True)
    internal_notes_encrypted = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return self.product_id

    def save(self, *args, **kwargs):
        # Encrypt Supplier Cost
        if self.supplier_cost_encrypted and not str(self.supplier_cost_encrypted).startswith('gAAAA'): 
            self.supplier_cost_encrypted = encrypt_value(self.supplier_cost_encrypted)
        
        # Encrypt Internal Notes
        if self.internal_notes_encrypted and not str(self.internal_notes_encrypted).startswith('gAAAA'): 
            self.internal_notes_encrypted = encrypt_value(self.internal_notes_encrypted)
            
        super().save(*args, **kwargs)
