from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def orders_view(request):
    print("Order Details")
    return HttpResponse("Order Details")
