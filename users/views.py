from django.shortcuts import render
from django.views.generic.base import View

def home(request):
    return render(request, 'about.html')

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