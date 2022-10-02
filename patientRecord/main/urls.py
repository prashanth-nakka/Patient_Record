from django.urls import path
from main import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add-patient', views.add_patient, name='add-patient'),
]
