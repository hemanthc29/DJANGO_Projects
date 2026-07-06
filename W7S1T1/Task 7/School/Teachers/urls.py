from django.urls import path
from .views import teachers_view

urlpatterns = [
    path('', teachers_view, name='teachers_view'),
]
