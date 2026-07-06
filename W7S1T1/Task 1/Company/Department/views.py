from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def department_view(request):
    print("This is Department")
    return HttpResponse("This is Department")
