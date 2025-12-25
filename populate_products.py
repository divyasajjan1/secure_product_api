import csv
import random
from datetime import datetime
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secure_product_api.settings")
django.setup()

from products.models import Product

CSV_FILE = "products.csv"

with open(CSV_FILE, newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # CSV uses tab delimiter
    for row in reader:
        product, created = Product.objects.get_or_create(
            product_id=row['product_id'],
            defaults={
                'product_category': row['product_category'],
                'product_price': float(row['product_price']),
                'product_manufacturing_date': datetime.strptime(row['product_manufacturing_date'], "%Y-%m-%d").date(),
                'product_expiry_date': datetime.strptime(row['product_expiry_date'], "%Y-%m-%d").date(),
                'supplier_cost': round(random.uniform(5, 500), 2),  # dummy encrypted value
                'internal_notes': f"Dummy note for {row['product_id']}"
            }
        )
        if created:
            print(f"Created product {product.product_id}")
        else:
            print(f"Product {product.product_id} already exists")
