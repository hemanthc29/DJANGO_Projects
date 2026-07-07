import subprocess
import time
import requests
import json
import sys

def main():
    print("Starting Django development server...")
    # Start Django server
    server_process = subprocess.Popen(
        [sys.executable, "manage.py", "runserver", "8000"],
        cwd="EmployeeManagement",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Wait for server to start
    time.sleep(3)
    
    base_url = "http://127.0.0.1:8000/employees/"
    
    employees_to_add = [
        {
            "name": "Rahul Sharma",
            "email": "rahul@gmail.com",
            "phone": "9876543210",
            "department": "Software Development",
            "designation": "Python Developer",
            "salary": 65000.0,
            "city": "Hyderabad"
        },
        {
            "name": "Priya Reddy",
            "email": "priya@gmail.com",
            "phone": "9123456789",
            "department": "Human Resources",
            "designation": "HR Executive",
            "salary": 45000.0,
            "city": "Bangalore"
        },
        {
            "name": "Arjun Kumar",
            "email": "arjun@gmail.com",
            "phone": "9988776655",
            "department": "Testing",
            "designation": "QA Engineer",
            "salary": 55000.0,
            "city": "Chennai"
        },
        {
            "name": "Sneha Patel",
            "email": "sneha@gmail.com",
            "phone": "9012345678",
            "department": "UI/UX",
            "designation": "UI Designer",
            "salary": 50000.0,
            "city": "Pune"
        },
        {
            "name": "Vikram Singh",
            "email": "vikram@gmail.com",
            "phone": "9090909090",
            "department": "DevOps",
            "designation": "DevOps Engineer",
            "salary": 70000.0,
            "city": "Mumbai"
        }
    ]
    
    try:
        # 1. Add employees
        print("\n--- 1. Adding 5 Employees (POST /employees/add/) ---")
        for i, emp in enumerate(employees_to_add, 1):
            response = requests.post(f"{base_url}add/", json=emp)
            print(f"POST Employee {i} Status Code:", response.status_code)
            print("Response:", json.dumps(response.json(), indent=2))
            
        # 2. View all employees
        print("\n--- 2. Viewing All Employees (GET /employees/) ---")
        response = requests.get(base_url)
        print("GET Status Code:", response.status_code)
        print("Response:", json.dumps(response.json(), indent=2))
        
        # 3. Update employee with ID = 2
        print("\n--- 3. Updating Employee ID 2 (PUT /employees/update/2/) ---")
        update_data = {
            "name": "Priya Reddy",
            "email": "priya.reddy@gmail.com",
            "phone": "9123456789",
            "department": "Human Resources",
            "designation": "Senior HR Executive",
            "salary": 55000.0,
            "city": "Hyderabad"
        }
        response = requests.put(f"{base_url}update/2/", json=update_data)
        print("PUT Status Code:", response.status_code)
        print("Response:", json.dumps(response.json(), indent=2))
        
        # 4. View all employees to confirm update
        print("\n--- 4. Viewing All Employees after Update (GET /employees/) ---")
        response = requests.get(base_url)
        print("GET Status Code:", response.status_code)
        print("Response:", json.dumps(response.json(), indent=2))
        
        # 5. Delete employee with ID = 2
        print("\n--- 5. Deleting Employee ID 2 (DELETE /employees/delete/2/) ---")
        response = requests.delete(f"{base_url}delete/2/")
        print("DELETE Status Code:", response.status_code)
        print("Response:", json.dumps(response.json(), indent=2))
        
        # 6. View all employees after delete
        print("\n--- 6. Viewing All Employees after Deletion (GET /employees/) ---")
        response = requests.get(base_url)
        print("GET Status Code:", response.status_code)
        print("Response:", json.dumps(response.json(), indent=2))

    except Exception as e:
        print("An error occurred during verification:", e)
    finally:
        print("\nTerminating Django server...")
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()
        print("Django server terminated.")

if __name__ == "__main__":
    main()
