from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def student(request):
    print("This is Student")
    accept = request.headers.get('Accept', '')
    if request.GET.get('format') == 'json' or ('application/json' in accept and 'text/html' not in accept):
        return JsonResponse({"message": "Welcome to Student App"})
    return render(request, 'student_home.html')

def student_details(request):
    print("Student Details Page")
    return JsonResponse({"message": "Student Details Page"})

def student_profile(request):
    print("Student Profile Page")
    return JsonResponse({"message": "Student Profile Page"})

def student_dynamic(request, id):
    msg = f"Student ID : {id}"
    print(msg)
    return JsonResponse({
        "message": msg,
        "Student ID": id
    })
