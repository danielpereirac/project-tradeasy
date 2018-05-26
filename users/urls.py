from django.urls import  include, path
from .views import home
from .views import about
from .views import register
from .views import story
from .views import postsign
from. views import login

urlpatterns = [
    path('about/', about, name='template_about'),
    path('story/', story, name='template_story'),
    path('register/', register, name='template_register'),
    path('', login, name='template_login'),
    path('home/', home, name='template_home'),
    path('postsign/',postsign)
]