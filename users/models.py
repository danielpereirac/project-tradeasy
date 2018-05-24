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

class Item(models.Model):
    title = models.CharField()
    description = models.CharField(max_length=10, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    created = models.DateField(auto_now=True)

class Transaction(models.Model):
    userOne = models.ForeignKey('User', on_delete=models.CASCADE)
    userTwo = models.ForeignKey('User', on_delete=models.CASCADE)
    itemOne = models.ForeignKey('Item', on_delete=models.CASCADE)
    itemTwo = models.ForeignKey('Item', on_delete=models.CASCADE)
    initialDate = models.DateField(auto_now=True)
    finalDate = models.DateField(auto_now=True)
    description = models.CharField(max_length=10, null=True)
    status = int

class Message(models.Model):
    byUser = int
    toUser = int
    transaction = models.CharField(max_length=10, null=True)
    message = models.CharField(max_length=10, null=True)
    date = models.DateField(auto_now=True)


