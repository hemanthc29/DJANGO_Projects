import urllib.request
import urllib.parse
import json
import sys

# Ensure UTF-8 output encoding for terminals
sys.stdout.reconfigure(encoding='utf-8')

base_url = "http://127.0.0.1:8000"

tests = [
    # Doctor template pages
    {"url": "/doctor/", "method": "GET", "expected_status": 200, "contains": ["Hospital Management System", "Welcome to Doctor Module"]},
    {"url": "/doctor/details/", "method": "GET", "expected_status": 200, "contains": ["Doctor Details", "Doctor ID : D101", "Doctor Name : Dr. Ramesh Kumar", "Specialization : Cardiologist", "Experience : 12 Years", "Hospital : City Hospital"]},
    {"url": "/doctor/profile/", "method": "GET", "expected_status": 200, "contains": ["Doctor Profile", "Qualification : MBBS, MD", "Department : Cardiology", "Available : Monday - Saturday", "Timing : 9 AM - 5 PM"]},
    {"url": "/doctor/contact/", "method": "GET", "expected_status": 200, "contains": ["Doctor Contact", "Email : ramesh@hospital.com", "Phone : 9876543210"]},

    # Patient template pages
    {"url": "/patient/", "method": "GET", "expected_status": 200, "contains": ["Hospital Management System", "Welcome to Patient Module"]},
    {"url": "/patient/details/", "method": "GET", "expected_status": 200, "contains": ["Patient Details", "Patient ID : P201", "Patient Name : Rahul Sharma", "Age : 28", "Gender : Male"]},
    {"url": "/patient/report/", "method": "GET", "expected_status": 200, "contains": ["Disease : Viral Fever", "Doctor : Dr. Ramesh Kumar", "Room : 203", "Status : Recovering"]},
    {"url": "/patient/bill/", "method": "GET", "expected_status": 200, "contains": ["Consultation : \u20b9500", "Medicine : \u20b9850", "Lab Test : \u20b91500", "Total : \u20b92850"]},

    # Dynamic URLs
    {"url": "/doctor/101/", "method": "GET", "expected_status": 200, "exact": "Doctor ID : 101"},
    {"url": "/doctor/Ramesh/", "method": "GET", "expected_status": 200, "exact": "Doctor Name : Ramesh"},
    {"url": "/patient/201/", "method": "GET", "expected_status": 200, "exact": "Patient ID : 201"},
    {"url": "/patient/Rahul/", "method": "GET", "expected_status": 200, "exact": "Patient Name : Rahul"},

    # Doctor REST APIs
    {"url": "/doctor/api/", "method": "GET", "expected_status": 200, "json": {"message": "Welcome to Doctor API"}},
    {"url": "/doctor/api/details/", "method": "GET", "expected_status": 200, "json": {
        "doctor_id": "D101",
        "doctor_name": "Dr. Ramesh Kumar",
        "specialization": "Cardiologist",
        "experience": "12 Years",
        "hospital": "City Hospital"
    }},
    {"url": "/doctor/api/add/", "method": "POST", "expected_status": 200, "json": {"message": "Doctor Added Successfully"}},
    {"url": "/doctor/api/update/", "method": "PUT", "expected_status": 200, "json": {"message": "Doctor Updated Successfully"}},
    {"url": "/doctor/api/delete/", "method": "DELETE", "expected_status": 200, "json": {"message": "Doctor Deleted Successfully"}},

    # Patient REST APIs
    {"url": "/patient/api/", "method": "GET", "expected_status": 200, "json": {"message": "Welcome to Patient API"}},
    {"url": "/patient/api/details/", "method": "GET", "expected_status": 200, "json": {
        "patient_id": "P201",
        "patient_name": "Rahul Sharma",
        "age": 28,
        "gender": "Male",
        "disease": "Viral Fever"
    }},
    {"url": "/patient/api/add/", "method": "POST", "expected_status": 200, "json": {"message": "Patient Added Successfully"}},
    {"url": "/patient/api/update/", "method": "PUT", "expected_status": 200, "json": {"message": "Patient Updated Successfully"}},
    {"url": "/patient/api/delete/", "method": "DELETE", "expected_status": 200, "json": {"message": "Patient Deleted Successfully"}},
]

failed = 0
passed = 0

for t in tests:
    url = base_url + t["url"]
    req = urllib.request.Request(url, method=t["method"])
    try:
        with urllib.request.urlopen(req) as res:
            status = res.status
            body = res.read().decode('utf-8')
            
            # Check Status
            if status != t["expected_status"]:
                print(f"[FAIL] {t['method']} {t['url']} - Status got {status}, expected {t['expected_status']}")
                failed += 1
                continue
                
            # Check content
            if "contains" in t:
                missing = [p for p in t["contains"] if p not in body]
                if missing:
                    print(f"[FAIL] {t['method']} {t['url']} - Missing content: {missing}")
                    failed += 1
                    continue
            
            if "exact" in t:
                clean_body = body.strip()
                if clean_body != t["exact"]:
                    print(f"[FAIL] {t['method']} {t['url']} - Got exact '{clean_body}', expected '{t['exact']}'")
                    failed += 1
                    continue
                    
            if "json" in t:
                try:
                    data = json.loads(body)
                    if data != t["json"]:
                        print(f"[FAIL] {t['method']} {t['url']} - JSON got {data}, expected {t['json']}")
                        failed += 1
                        continue
                except Exception as ex:
                    print(f"[FAIL] {t['method']} {t['url']} - Response body not valid JSON: {ex}")
                    failed += 1
                    continue
            
            print(f"[PASS] {t['method']} {t['url']}")
            passed += 1
            
    except Exception as e:
        print(f"[FAIL] {t['method']} {t['url']} - Exception: {e}")
        failed += 1

print(f"\n--- Result: {passed} passed, {failed} failed ---")
if failed > 0:
    exit(1)
else:
    exit(0)
