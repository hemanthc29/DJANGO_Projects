from django.urls import path
from .views import classes_view

urlpatterns = [
    path('', classes_view, name='classes_view'),
]
