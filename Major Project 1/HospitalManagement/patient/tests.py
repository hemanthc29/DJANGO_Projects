from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Patient

class PatientAPITests(APITestCase):
    def setUp(self):
        self.patient1_data = {
            "patient_name": "Rahul Sharma",
            "age": 28,
            "gender": "Male",
            "phone": "9123456789",
            "disease": "Fever",
            "address": "Hyderabad"
        }
        self.patient2_data = {
            "patient_name": "Sneha Patel",
            "age": 34,
            "gender": "Female",
            "phone": "9988776655",
            "disease": "Skin Allergy",
            "address": "Bangalore"
        }
        self.patient = Patient.objects.create(**self.patient1_data)

    def test_create_patient(self):
        url = reverse('add_patient')
        response = self.client.post(url, self.patient2_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 2)
        self.assertEqual(Patient.objects.get(id=response.data['id']).patient_name, "Sneha Patel")

    def test_get_patients(self):
        url = reverse('get_patients')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_patient(self):
        url = reverse('update_patient', kwargs={'id': self.patient.id})
        updated_data = self.patient1_data.copy()
        updated_data['disease'] = "Malaria"
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.disease, "Malaria")

    def test_delete_patient(self):
        url = reverse('delete_patient', kwargs={'id': self.patient.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Patient.objects.count(), 0)
