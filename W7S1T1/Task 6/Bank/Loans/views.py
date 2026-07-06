from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loans_view(request):
    print("Loan Details")
    return HttpResponse("Loan Details")
