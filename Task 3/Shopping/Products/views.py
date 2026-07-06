from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def products_view(request):
    print("Welcome to Products")
    return HttpResponse("Welcome to Products")
