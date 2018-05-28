from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import pyrebase
from django.contrib import auth


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

def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('Password')
    try:
        user=authe.create_user_with_email_and_password(email,password)

    except:
        return render(request, "register_error.html")

    uid=user['localId']
    data={"name":name , "status":"1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request, "success_register.html")
    

def itemdetail(request):
    return render(request, 'item-detail.html')

def itemhorizon(request):
    return render(request, 'item-games.html')

def signin(request):
    return render(request)

def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        user = authe.sign_in_with_email_and_password(email,password)
    except:
        return render(request, "login_error.html")
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    print(user)
    return render(request, "home.html", {"email":email})

def logout (request):
    auth.logout(request)
    return render(request, 'login.html')





def login(request):
    return render(request, 'login.html')

def loginerror(request):
    return render(request, 'loginerror.html')

def registererror(request):
    return render(request, 'register_error.html')

def successregister(request):
    return render(request, 'success_register.html')

def forgotpass(request):
    return render(request, 'forgotpass.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def story(request):
    return render(request, 'story.html')
