import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_inventory_project.settings')
django.setup()

from django.test import Client

def run_tests():
    client = Client()

    print("--- 1. Testing view all products (GET /products/) ---")
    response = client.get('/products/')
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
    print()

    print("--- 2. Testing add product (POST /products/add/) ---")
    new_product = {
        "product_name": "Wireless Mouse",
        "category": "Electronics",
        "brand": "Logitech",
        "price": 899,
        "quantity": 50,
        "supplier": "ABC Distributors"
    }
    response = client.post('/products/add/', data=json.dumps(new_product), content_type='application/json')
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
    print()
    added_product_id = response.json()['product']['id']

    print(f"--- 3. Testing update product (PUT /products/update/{added_product_id}/) ---")
    updated_product = {
        "product_name": "Wireless Mouse",
        "category": "Electronics",
        "brand": "Logitech",
        "price": 999,
        "quantity": 45,
        "supplier": "ABC Distributors"
    }
    response = client.put(f'/products/update/{added_product_id}/', data=json.dumps(updated_product), content_type='application/json')
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
    print()

    print(f"--- 4. Testing delete product (DELETE /products/delete/{added_product_id}/) ---")
    response = client.delete(f'/products/delete/{added_product_id}/')
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
    print()

    print("--- 5. Testing view all products after operations (GET /products/) ---")
    response = client.get('/products/')
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    run_tests()
