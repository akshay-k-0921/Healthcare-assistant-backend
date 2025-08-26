from django.db import models

class Symptom(models.Model):
    name = models.CharField(max_length=100)

class SymptomRecord(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class DoctorSuggestion(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    doctor_specialty = models.CharField(max_length=100)
