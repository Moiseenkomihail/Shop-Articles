from django.urls import path, include
from .views import *
from .models import *


urlpatterns = [
    path('create_news', CreateNewsView.as_view(), name='create_news')
]
