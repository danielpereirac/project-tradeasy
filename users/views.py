from django.shortcuts import render
from django.views.generic.base import View
import pyrebase


config = {
	'apiKey': "AIzaSyDzTe7Y8MsnyyvEtP_IOOPf6TPCl3nnVJ0",
	'authDomain': "tradeasy-202920.firebaseapp.com",
	'databaseURL': "https://tradeasy-202920.firebaseio.com",
	'projectId': "tradeasy-202920",
	'storageBucket': "tradeasy-202920.appspot.com",
	'messagingSenderId': "546787020187"
	}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def singin(request):
    return render(request)

def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get('password')

    user = auth.sign_in_with_email_and_password(email,password)

    return render(request, "about.html")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def story(request):
    return render(request, 'story.html')


class HomeUserView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class RegisterUserView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class AboutUserView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class StoryUserView(View):
    template_name = 'story.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)