from django.urls import path, include
from .views import *
from .models import *


urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('create_article/', CreateArticleView.as_view(), name='create_article'),
    path('articles/<int:id>', DetailArticleView, name='article'),
]
