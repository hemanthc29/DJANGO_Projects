from django.urls import path
from .views import restaurants_view

urlpatterns = [
    path('', restaurants_view, name='restaurants_view'),
]
