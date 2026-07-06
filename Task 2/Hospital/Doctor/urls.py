from django.urls import path
from .views import doctor_view

urlpatterns = [
    path('', doctor_view, name='doctor_view'),
]
