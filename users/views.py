from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User
import pyrebase
from users.models import Cloth
from users.models import Card
from users.models import Book
from users.models import Games
from users.models import Item




config = {
	'apiKey': "AIzaSyDzTe7Y8MsnyyvEtP_IOOPf6TPCl3nnVJ0",
	'authDomain': "tradeasy-202920.firebaseapp.com",
	'databaseURL': "https://tradeasy-202920.firebaseio.com/",
	'projectId': "tradeasy-202920",
	'storageBucket': "tradeasy-202920.appspot.com",
	'messagingSenderId': "546787020187"
	}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()
user=None

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user=authe.create_user_with_email_and_password(email,password)
        user=User.objects.create_user(name,email,password)
    except:
        return render(request, "register_error.html")

    return render(request, "success_register.html")


def itemdetail(request):
    return render(request, 'item-detail.html')

def itemhorizon(request):
    return render(request, 'item-games.html')

def signin(request):
    return render(request)

def postsign(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            usuario_aux = User.objects.get(email = email)
            userPyrebase = authe.sign_in_with_email_and_password(email,password)
            usuario = authenticate(request, username=usuario_aux.username,password=password)
            if usuario:
                login(request, usuario)
                return home(request)

        except:
            return render(request, "login_error.html")

    print("final")
    return render(request, "home.html")

def logoutPage (request):
    auth.logout(request)
    logout(request)
    return render(request, 'login.html')


def loginerror(request):
    return render(request, 'loginerror.html')

def loginPage(request):
    return render(request, 'login.html')

def registererror(request):
    return render(request, 'register_error.html')

def successregister(request):
    return render(request, 'success_register.html')

def forgotpass(request):
    return render(request, 'forgotpass.html')

def home(request):
    itens =Item.objects.all()
    
    context = {
        "itens": itens,
        }
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def story(request):
    return render(request, 'story.html')

def faq(request):
    return render(request, 'faq.html')

def howtotrade(request):
    return render(request, 'howtotrade.html')

def profile(request):
    itens = Item.objects.filter(user=request.user)
    context = {
        "itens": itens,
        }
    return render(request, 'profile.html', context)

def registeritem(request):
    return render(request, 'register-item.html')


def registercloth(request):
    
    categories= request.POST.get('categories')
    
    if categories=='clothes':
        title = request.POST.get('Title')
        description = request.POST.get('Description')
        size = request.POST.get('Size')
        color = request.POST.get('Color')
        brand = request.POST.get('Brand')        
        clothAdd = Cloth.objects.create(title=title, description=description,image='../static/img/tshirt.jpg',size=size,color=color,brand=brand,user=request.user)
        
        
    if categories=='card':
        
        title = request.POST.get('Title')
        description = request.POST.get('Description')
        collection = request.POST.get('CollectionCard')
        edition = request.POST.get('Edition')
        color = request.POST.get('Color')
        
        cardAdd = Card.objects.create(title=title, description=description,image='../static/img/copa.jpg',collection=collection,edition=edition,color=color,user=request.user)
        
    
    if categories=='books':
        title = request.POST.get('Title')
        description = request.POST.get('Description')
        author = request.POST.get('Author')
        language = request.POST.get('Language')
        country = request.POST.get('Country')
        genre = request.POST.get('Genre')
        publisher = request.POST.get('Publisher')        
        bookAdd = Book.objects.create(title=title, description=description,image='../static/img/livro.jpg',author=author,language=language,country=country,genre=genre,publisher=publisher,user=request.user)


    if categories=='games':
        title = request.POST.get('Title')
        description = request.POST.get('Description')
        publisher = request.POST.get('Collection')
        plataform = request.POST.get('Plataform')
        series = request.POST.get('Series')
        release = request.POST.get('Release')
        gameAdd = Games.objects.create(title=title, description=description,image='../static/img/gears.jpeg',publisher=publisher,plataform=plataform,series=series,releaseDate=release,user=request.user)
        gameAdd.save()
       
    return home(request)


