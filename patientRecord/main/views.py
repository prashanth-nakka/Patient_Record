from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Pateint
from .forms import PatientForm
# Create your views here.

# HOME


def home(request):
    data = Pateint.objects.all()
    if "q" in request.GET:
        q = request.GET['q']
        data = Pateint.objects.filter(Q(full_name__icontains=q) | Q(
            mobile_no__icontains=q) | Q(email__icontains=q))
    paginatior = Paginator(data,10)
    page_number = request.GET.get('page', 1)
    data = paginatior.get_page(page_number)
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

# SEND EMAIL


def send_email(request, id):
    patient_id = Pateint.objects.get(id=id)
    send_mail(
        'Next Visit Remainder',
        'Your Next Visit is on: ' + str(patient_id.next_visit_date),
        'adim@mail.com',
        [patient_id.email],
        fail_silently=False,
    )
    messages.success(request, f"Email has been sent to {patient_id.email}")
    return redirect('/')
