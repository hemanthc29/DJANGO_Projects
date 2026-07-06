from django.urls import path
from .views import trainers_view

urlpatterns = [
    path('', trainers_view, name='trainers_view'),
]
