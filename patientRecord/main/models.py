from django.db import models

# Create your models here.


class Pateint(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    detail = models.TextField()
    precount = models.TextField()
    visit_date = models.DateTimeField(auto_now_add=True)
    next_visit_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.full_name
