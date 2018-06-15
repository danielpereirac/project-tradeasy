
from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=10, null=False)
    image = models.FileField(null=True,blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cloth(Item):

    top = 1
    body = 2
    pants = 3
    shoes = 4
    acessories = 5

    types = [
        (top , "Top"),
        (body, "Body"),
        (pants, "Pants"),
        (shoes, "Shoes"),
        (acessories, "Acessories"),        
    ]

    tipology = models.IntegerField(choices=types, default=1)
    size = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=20, null=True)
    collection = models.CharField(max_length=20, null=True)

class Book(Item):

    thriller = 1
    biography = 2
    comics = 3
    fantasy = 4
    science = 5
    romance = 6

    types = [        
    (thriller , "Thriller"),
    (biography , "Biography"),
    (comics , "Comics"),
    (fantasy , "Fantasy"),
    (science , "Science"),
    (romance , "Romance"),
    ]

    tipology = models.IntegerField(choices=types,default=1)
    author = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    language = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=20, null=True)
    publisher = models.CharField(max_length=20, null=True)
    publicationDate = models.DateTimeField()
    pages = int
    edition = int
    
class Games(Item):

    ps4 = 1
    xboxone = 2
    nintengowiiu = 3
    nintendoswitch = 4

    types = [            
    (ps4 , "PS4"),
    (xboxone , "Xbox-One"),
    (nintengowiiu , "Nintendo Wii U"),
    (nintendoswitch , "Nintendo Switch"),
    ]

    tipology = models.IntegerField(choices=types,default=1)
    plataform = models.CharField(max_length=20, null=False)
    series = models.CharField(max_length=20, null=True)
    releaseDate = models.CharField(max_length=20, null=True)
    publisher = models.CharField(max_length=20, null=True)

class Card(Item):

    magic = 1
    yugioh = 2
    pokemon = 3

    types = [            
    (magic , "Magic The Gathering"),
    (yugioh , "Yugi-Oh"),
    (pokemon , "Pokemon"),
    ]

    tipology = models.IntegerField(choices=types,default=1)
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



