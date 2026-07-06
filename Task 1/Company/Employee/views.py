from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employee_view(request):
    print("This is Employee")
    return HttpResponse("This is Employee")
