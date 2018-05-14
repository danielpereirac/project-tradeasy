from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=10, null=False)
    birth = models.DateField(null=True)
    cep = models.CharField(max_length=12, null=False)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    idTransaction = 1