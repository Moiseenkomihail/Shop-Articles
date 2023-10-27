from django.urls import path, include
from .views import *
from .models import *


urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', log_out, name='log_out'),
    path('login/', log_in, name='log_in'),
    path('profile', user_profile, name='profile')
]
