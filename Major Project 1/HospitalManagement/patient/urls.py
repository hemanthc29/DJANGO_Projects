from django.urls import path
from . import views

urlpatterns = [
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/', views.get_patients, name='get_patients'),
    path('patients/update/<int:id>/', views.update_patient, name='update_patient'),
    path('patients/delete/<int:id>/', views.delete_patient, name='delete_patient'),
]
