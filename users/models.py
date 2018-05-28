from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=10, null=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.email

class Item(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=10, null=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)


# class Category(Item):

class Book(Item):
    author = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    language = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=20, null=True)
    publisher = models.CharField(max_length=20, null=True)
    publicationDate = models.DateTimeField()
    pages = int
    edition = int

class Cloth(Item):
    size = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=20, null=True)
    collection = models.CharField(max_length=20, null=True)

class Games(Item):
    plataform = models.CharField(max_length=20, null=False)
    series = models.CharField(max_length=20, null=True)
    releaseDate = models.CharField(max_length=20, null=True)

class Card(Item):
    collection = models.CharField(max_length=20, null=False)
    edition = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=20, null=True)

    

# class Transaction(models.Model):
#     userOne = models.ForeignKey('User', on_delete=models.CASCADE)
#     userTwo = models.ForeignKey('User', on_delete=models.CASCADE)
#     itemOne = models.ForeignKey('Item', on_delete=models.CASCADE)
#     itemTwo = models.ForeignKey('Item', on_delete=models.CASCADE)
#     initialDate = models.DateTimeField(auto_now=False, auto_now_add=True)
#     finalDate = models.DateTimeField(auto_now=True)
#     description = models.CharField(max_length=10, null=True)
#     status = int

# class Message(models.Model):
#     byUser = int
#     toUser = int
#     transaction = models.CharField(max_length=10, null=True)
#     message = models.CharField(max_length=10, null=True)
#     date = models.DateTimeField(auto_now=False, auto_now_add=True)



