from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Doctor

class DoctorAPITests(APITestCase):
    def setUp(self):
        self.doctor1_data = {
            "doctor_name": "Dr. Ramesh Kumar",
            "specialization": "Cardiologist",
            "experience": 12,
            "phone": "9876543210",
            "email": "ramesh@gmail.com",
            "consultation_fee": 700
        }
        self.doctor2_data = {
            "doctor_name": "Dr. Priya Sharma",
            "specialization": "Dermatologist",
            "experience": 8,
            "phone": "9876543222",
            "email": "priya@gmail.com",
            "consultation_fee": 500
        }
        self.doctor = Doctor.objects.create(**self.doctor1_data)

    def test_create_doctor(self):
        url = reverse('add_doctor')
        response = self.client.post(url, self.doctor2_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 2)
        self.assertEqual(Doctor.objects.get(id=response.data['id']).doctor_name, "Dr. Priya Sharma")

    def test_get_doctors(self):
        url = reverse('get_doctors')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_doctor(self):
        url = reverse('update_doctor', kwargs={'id': self.doctor.id})
        updated_data = self.doctor1_data.copy()
        updated_data['experience'] = 13
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.doctor.refresh_from_db()
        self.assertEqual(self.doctor.experience, 13)

    def test_delete_doctor(self):
        url = reverse('delete_doctor', kwargs={'id': self.doctor.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doctor.objects.count(), 0)
