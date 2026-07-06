from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members_view(request):
    print("Member Information")
    return HttpResponse("Member Information")
