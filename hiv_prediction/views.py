from django.conf import settings
from django.shortcuts import render
import numpy as np

def predict_hiv_diagnosis(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        gender = bool(request.POST['gender'])
        hiv_diagnoses = int(request.POST['hiv_diagnoses'])
        linked_to_care = float(request.POST['linked_to_care'])
        plwdhi_prevalence = float(request.POST['plwdhi_prevalence'])

        model = settings.MODEL

        x = [gender, age, hiv_diagnoses, linked_to_care, plwdhi_prevalence]
        x = np.array(x).reshape((1, -1))

        prediction = model.predict(x)

        if prediction[0] > 0.5:
            return 'HIV Diagnosis'
        return 'No HIV Diagnosis'

    return render(request)
