from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def faculty(request):
    print("This is Faculty")
    accept = request.headers.get('Accept', '')
    if request.GET.get('format') == 'json' or ('application/json' in accept and 'text/html' not in accept):
        return JsonResponse({"message": "Welcome to Faculty App"})
    return render(request, 'faculty_home.html')

def faculty_details(request):
    print("Faculty Details Page")
    return JsonResponse({"message": "Faculty Details Page"})

def faculty_profile(request):
    print("Faculty Profile Page")
    return JsonResponse({"message": "Faculty Profile Page"})

def faculty_dynamic(request, name):
    msg = f"Faculty Name : {name}"
    print(msg)
    return JsonResponse({
        "message": msg,
        "Faculty Name": name
    })
