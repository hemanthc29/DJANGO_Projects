from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def doctor_view(request):
    print("This is Doctor")
    return HttpResponse("This is Doctor")
