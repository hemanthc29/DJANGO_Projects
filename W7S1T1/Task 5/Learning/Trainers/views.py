from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trainers_view(request):
    print("Trainer Dashboard")
    return HttpResponse("Trainer Dashboard")
