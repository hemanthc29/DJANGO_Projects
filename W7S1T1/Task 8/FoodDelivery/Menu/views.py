from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_view(request):
    print("Food Menu")
    return HttpResponse("Food Menu")
