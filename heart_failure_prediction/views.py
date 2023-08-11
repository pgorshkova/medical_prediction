from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import PatientForm
from .utils import make_cancer_prediction


def index_form(request):
    """View-function to render form and return result."""
    if request.method == 'GET':
        form = PatientForm()
        context = {
            'form': form
        }
        return render(request, template_name='index.html', context=context)
    form = PatientForm(request.POST)
    if form.is_valid():
        form.save()
        data = [int(field.data) for field in list(form)[1:]]
        prediction = make_cancer_prediction(data)
        return HttpResponse(prediction)
