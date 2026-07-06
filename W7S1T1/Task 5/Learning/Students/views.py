from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students_view(request):
    print("Student Dashboard")
    return HttpResponse("Student Dashboard")
