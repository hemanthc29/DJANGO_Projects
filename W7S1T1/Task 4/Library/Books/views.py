from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def books_view(request):
    print("Book Information")
    return HttpResponse("Book Information")
