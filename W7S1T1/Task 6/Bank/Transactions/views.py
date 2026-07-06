from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def transactions_view(request):
    print("Transaction History")
    return HttpResponse("Transaction History")
