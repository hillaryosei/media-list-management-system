from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    specialty = models.CharField(max_length=200)
    publication = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    phone = PhoneNumberField(blank=False, null=True)


    def __str__(self):
        return f'Contact: {self.first_name} {self.last_name}'