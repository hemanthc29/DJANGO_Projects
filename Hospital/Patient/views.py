from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Template Views
def patient_home(request):
    return render(request, 'patient.html')

def patient_details(request):
    context = {
        'patient_id': 'P201',
        'patient_name': 'Rahul Sharma',
        'age': 28,
        'gender': 'Male'
    }
    return render(request, 'patient_details.html', context)

def patient_report(request):
    context = {
        'disease': 'Viral Fever',
        'doctor': 'Dr. Ramesh Kumar',
        'room': '203',
        'status': 'Recovering'
    }
    return render(request, 'patient_report.html', context)

def patient_bill(request):
    context = {
        'consultation': 500,
        'medicine': 850,
        'lab_test': 1500,
        'total': 2850
    }
    return render(request, 'patient_bill.html', context)

# Dynamic URL Views
def patient_id_view(request, patient_id):
    return HttpResponse(f"Patient ID : {patient_id}", content_type="text/plain")

def patient_name_view(request, patient_name):
    return HttpResponse(f"Patient Name : {patient_name}", content_type="text/plain")

# REST API Views
def patient_home_api(request):
    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Welcome to Patient API"})

def patient_details_api(request):
    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({
        "patient_id": "P201",
        "patient_name": "Rahul Sharma",
        "age": 28,
        "gender": "Male",
        "disease": "Viral Fever"
    })

@csrf_exempt
def add_patient_api(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Patient Added Successfully"})

@csrf_exempt
def update_patient_api(request):
    if request.method != 'PUT':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Patient Updated Successfully"})

@csrf_exempt
def delete_patient_api(request):
    if request.method != 'DELETE':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Patient Deleted Successfully"})
