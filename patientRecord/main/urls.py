from django.urls import path
from main import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add-patient', views.add_patient, name='add-patient'),
    path('update-patient/<int:id>', views.update_patient, name='update-patient'),
    path('delete-patient/<int:id>', views.delete_patient, name='delete-patient'),
    path('send-email/<int:id>', views.send_email, name='send-email'),
]
