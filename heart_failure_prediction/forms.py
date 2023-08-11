from django.forms import ModelForm

from .models import Patient


class PatientForm(ModelForm):
    """Patient form for rendering."""
    class Meta:
        model = Patient
        fields = '__all__'