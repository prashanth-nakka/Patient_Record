from django.shortcuts import redirect, render
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
            messages.success(request, "Pateint Details Added Successfully!")
    return render(request, 'add-patient.html', {'form': form})


# UPDATE PATIENT
def update_patient(request, id):
    patient_id = Pateint.objects.get(id=id)
    if request.method == 'POST':
        saveForm = PatientForm(request.POST, instance=patient_id)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request, "Patient Details Updated Successfully!")
        else:
            messages.error(request, "Patient Details Not Found!")
    form = PatientForm(instance=patient_id)
    return render(request, 'update-patient.html', {'form': form})

# DELETE PATEINT


def delete_patient(request, id):
    patient_id = Pateint.objects.filter(id=id)
    if patient_id:
        patient_id.delete()
    return redirect('/')
