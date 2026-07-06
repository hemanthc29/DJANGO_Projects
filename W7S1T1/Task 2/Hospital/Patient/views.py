from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def patient_view(request):
    print("This is Patient")
    return HttpResponse("This is Patient")
