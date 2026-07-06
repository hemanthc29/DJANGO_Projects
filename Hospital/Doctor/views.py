from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Template Views
def doctor_home(request):
    return render(request, 'doctor.html')

def doctor_details(request):
    context = {
        'doctor_id': 'D101',
        'doctor_name': 'Dr. Ramesh Kumar',
        'specialization': 'Cardiologist',
        'experience': '12 Years',
        'hospital': 'City Hospital'
    }
    return render(request, 'doctor_details.html', context)

def doctor_profile(request):
    context = {
        'qualification': 'MBBS, MD',
        'department': 'Cardiology',
        'availability': 'Monday - Saturday',
        'timing': '9 AM - 5 PM'
    }
    return render(request, 'doctor_profile.html', context)

def doctor_contact(request):
    context = {
        'email': 'ramesh@hospital.com',
        'phone': '9876543210'
    }
    return render(request, 'doctor_contact.html', context)

# Dynamic URL Views
def doctor_id_view(request, doctor_id):
    return HttpResponse(f"Doctor ID : {doctor_id}", content_type="text/plain")

def doctor_name_view(request, doctor_name):
    return HttpResponse(f"Doctor Name : {doctor_name}", content_type="text/plain")

# REST API Views
def doctor_home_api(request):
    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Welcome to Doctor API"})

def doctor_details_api(request):
    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({
        "doctor_id": "D101",
        "doctor_name": "Dr. Ramesh Kumar",
        "specialization": "Cardiologist",
        "experience": "12 Years",
        "hospital": "City Hospital"
    })

@csrf_exempt
def add_doctor_api(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Doctor Added Successfully"})

@csrf_exempt
def update_doctor_api(request):
    if request.method != 'PUT':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Doctor Updated Successfully"})

@csrf_exempt
def delete_doctor_api(request):
    if request.method != 'DELETE':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"message": "Doctor Deleted Successfully"})
