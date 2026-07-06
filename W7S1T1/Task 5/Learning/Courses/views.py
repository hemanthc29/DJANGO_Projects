from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses_view(request):
    print("Available Courses")
    return HttpResponse("Available Courses")
