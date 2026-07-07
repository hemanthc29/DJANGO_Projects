from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Appointment

class AppointmentAPITests(APITestCase):
    def setUp(self):
        self.appointment1_data = {
            "patient_name": "Rahul Sharma",
            "doctor_name": "Dr. Ramesh Kumar",
            "appointment_date": "2026-07-20",
            "appointment_time": "10:30:00",
            "status": "Confirmed"
        }
        self.appointment2_data = {
            "patient_name": "Sneha Patel",
            "doctor_name": "Dr. Priya Sharma",
            "appointment_date": "2026-07-21",
            "appointment_time": "02:00:00",
            "status": "Pending"
        }
        self.appointment = Appointment.objects.create(**self.appointment1_data)

    def test_create_appointment(self):
        url = reverse('add_appointment')
        response = self.client.post(url, self.appointment2_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 2)
        self.assertEqual(Appointment.objects.get(id=response.data['id']).patient_name, "Sneha Patel")

    def test_get_appointments(self):
        url = reverse('get_appointments')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_appointment(self):
        url = reverse('update_appointment', kwargs={'id': self.appointment.id})
        updated_data = self.appointment1_data.copy()
        updated_data['status'] = "Completed"
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, "Completed")

    def test_delete_appointment(self):
        url = reverse('delete_appointment', kwargs={'id': self.appointment.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Appointment.objects.count(), 0)
