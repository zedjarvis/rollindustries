from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}   :   {self.date}'
