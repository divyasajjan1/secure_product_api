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

def populate():
    with open(CSV_FILE, newline='') as csvfile:
        # If your CSV uses commas, keep it as is. If it uses tabs, add delimiter='\t'
        reader = csv.DictReader(csvfile) 
        
        for row in reader:
            # Generate some random sensitive data to test the encryption
            random_cost = str(round(random.uniform(10, 500), 2))
            random_note = f"Sensitive supplier info for {row['product_id']}"

            product, created = Product.objects.update_or_create(
                product_id=row['product_id'],
                defaults={
                    'product_category': row['product_category'],
                    'product_price': float(row['product_price']),
                    'product_manufacturing_date': datetime.strptime(row['product_manufacturing_date'], "%Y-%m-%d").date(),
                    'product_expiry_date': datetime.strptime(row['product_expiry_date'], "%Y-%m-%d").date(),
                    
                    # Pass PLAIN TEXT here. 
                    # Your Model's save() method will detect these and encrypt them!
                    'supplier_cost_encrypted': random_cost,
                    'internal_notes_encrypted': random_note
                }
            )
            
            if created:
                print(f"✅ Created: {product.product_id}")
            else:
                print(f"🔄 Updated: {product.product_id} with new encrypted data")

if __name__ == '__main__':
    populate()
