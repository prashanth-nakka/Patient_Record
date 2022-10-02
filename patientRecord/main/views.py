from django.shortcuts import render
from django.contrib import messages
from .models import Pateint
from .forms import PatientForm
# Create your views here.


def home(request):
    data = Pateint.objects.all()
    context = {'data': data}
    return render(request, 'home.html', context)

# ADD PATIENT


def add_patient(request):
    form = PatientForm
    if request.method == 'POST':
        saveForm = PatientForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request, "Pateint Added Successfully!")
    return render(request, 'add-patient.html', {'form': form})
