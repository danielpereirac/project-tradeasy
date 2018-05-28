from django.urls import  include, path
from .views import home
from .views import about
from .views import register
from .views import story
from .views import postsign
from .views import postsignup
from. views import login
from. views import forgotpass
from. views import loginerror
from. views import registererror
from. views import successregister
from .views import logout
from .views import itemdetail
from .views import itemhorizon

urlpatterns = [
    path('about/', about, name='template_about'),
    path('story/', story, name='template_story'),
    path('register/', register, name='template_register'),
    path('', login, name='template_login'),
    path('home/', home, name='template_home'),
    path('postsign/',postsign),
    path('postsignup/', postsignup, name='template_signup'),
    path('forgotpass/', forgotpass, name='template_forgotpass'),
    path('loginerror/', loginerror),
    path('logout/', logout, name='template_logout'),
    path('itemdetails/', itemdetail, name='template_livro'),
    path('itemhorizon/', itemhorizon, name='template_horizon')
]