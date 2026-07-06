from django.urls import path
from .views import patient_view

urlpatterns = [
    path('', patient_view, name='patient_view'),
]
