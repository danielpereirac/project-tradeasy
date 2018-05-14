from django.urls import  include, path
from .views import home

urlpatterns = [
    # path(r'^register/$', views.RegisterUserView.as_view(), name="register"),
    # path(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
    # path(r'^about/$',     views.AboutUserView.as_view(), name="about"),
    path('', home),
]