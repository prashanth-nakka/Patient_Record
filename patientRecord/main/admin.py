from django.contrib import admin
from .models import Pateint
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_no',
                    'detail', 'visit_date', 'next_visit_date')
    search_fields = ('full_name', 'email', 'mobile_no',)


admin.site.register(Pateint, PatientAdmin)
