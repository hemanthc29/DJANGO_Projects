import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_inventory_project.settings')
django.setup()

from products.models import Product

def seed_database():
    print("Clearing existing products...")
    Product.objects.all().delete()

    products_data = [
        {
            "product_name": "Wireless Mouse",
            "category": "Electronics",
            "brand": "Logitech",
            "price": 899,
            "quantity": 50,
            "supplier": "ABC Distributors"
        },
        {
            "product_name": "Mechanical Keyboard",
            "category": "Electronics",
            "brand": "Redragon",
            "price": 2499,
            "quantity": 20,
            "supplier": "XYZ Suppliers"
        },
        {
            "product_name": "USB-C Charger",
            "category": "Accessories",
            "brand": "Samsung",
            "price": 1499,
            "quantity": 35,
            "supplier": "Tech World"
        },
        {
            "product_name": "Gaming Headset",
            "category": "Electronics",
            "brand": "HyperX",
            "price": 3999,
            "quantity": 15,
            "supplier": "Gaming Store"
        },
        {
            "product_name": "External Hard Disk",
            "category": "Storage",
            "brand": "Seagate",
            "price": 5499,
            "quantity": 10,
            "supplier": "Digital Hub"
        }
    ]

    for item in products_data:
        prod = Product.objects.create(**item)
        print(f"Added product: {prod.product_name} (ID: {prod.id})")

if __name__ == "__main__":
    seed_database()
