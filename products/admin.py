from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Columns to show in the main list table
    list_display = (
        'product_id', 
        'product_category', 
        'product_price', 
        'supplier_cost_encrypted', 
        'internal_notes_encrypted'
    )

    # Search bar for quick filtering
    search_fields = ('product_id', 'product_category')

    # Sidebar filters
    list_filter = ('product_category', 'product_manufacturing_date')

    # Organizes the detail view when you click on a product
    fieldsets = (
        ('Basic Information', {
            'fields': ('product_id', 'product_category', 'product_price')
        }),
        ('Dates', {
            'fields': ('product_manufacturing_date', 'product_expiry_date')
        }),
        ('Sensitive Data (Encrypted)', {
            'description': 'These fields are stored as ciphertext in the database.',
            'fields': ('supplier_cost_encrypted', 'internal_notes_encrypted'),
        }),
    )