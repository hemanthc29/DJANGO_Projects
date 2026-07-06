from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def restaurants_view(request):
    print("Restaurant List")
    return HttpResponse("Restaurant List")
