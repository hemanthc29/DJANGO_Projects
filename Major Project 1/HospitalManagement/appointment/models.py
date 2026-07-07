from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.patient_name} with {self.doctor_name} on {self.appointment_date}"
