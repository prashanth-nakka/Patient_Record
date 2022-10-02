from django.shortcuts import render
from .models import Pateint
# Create your views here.


def home(request):
    data = Pateint.objects.all()
    context = {'data': data}
    return render(request, 'home.html', context)
