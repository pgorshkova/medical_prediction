from django.db import models

class HIVInput(models.Model):
    age = models.IntegerField()
    gender = models.BooleanField()
    hiv_diagnoses = models.IntegerField()
    linked_to_care = models.FloatField()
    plwdhi_prevalence = models.FloatField()