from django.urls import path
from . import views

urlpatterns = [
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/', views.get_doctors, name='get_doctors'),
    path('doctors/update/<int:id>/', views.update_doctor, name='update_doctor'),
    path('doctors/delete/<int:id>/', views.delete_doctor, name='delete_doctor'),
]
