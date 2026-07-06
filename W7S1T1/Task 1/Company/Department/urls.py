from django.urls import path
from .views import department_view

urlpatterns = [
    path('', department_view, name='department_view'),
]
