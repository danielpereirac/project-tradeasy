from django.urls import  include, path
from .views import home
from .views import about
from .views import register
from .views import story
from .views import postsign
from .views import postsignup
from. views import forgotpass
from. views import loginPage
from. views import loginerror
from. views import registererror
from. views import successregister
from .views import logoutPage
from .views import itemdetail
from .views import itemhorizon
from .views import faq
from .views import howtotrade
from .views import registeritem
from .views import profile
from .views import registercloth


urlpatterns = [
    path('about/', about, name='template_about'),
    path('story/', story, name='template_story'),
    path('faq/', faq, name='template_faq'),
    path('howtotrade/', howtotrade, name='template_howtotrade'),
    path('register/', register, name='template_register'),
    path('', loginPage, name='template_login'),
    path('home/', home, name='template_home'),
    path('postsign/',postsign),
    path('postsignup/', postsignup, name='template_signup'),
    path('forgotpass/', forgotpass, name='template_forgotpass'),
    path('loginerror/', loginerror),
    path('logout/', logoutPage, name='template_logout'),
    path('itemdetails/', itemdetail, name='template_livro'),
    path('itemhorizon/', itemhorizon, name='template_horizon'),
    path('registeritem/', registeritem, name='template_registeritem'),
    path('profile/', profile, name='template_profile'),
    path('registercloth/', registercloth)
]