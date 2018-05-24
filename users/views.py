from django.shortcuts import render
from django.views.generic.base import View

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def story(request):
    return render(request, 'story.html')



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