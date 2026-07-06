from django.urls import path
from .views import loans_view

urlpatterns = [
    path('', loans_view, name='loans_view'),
]
