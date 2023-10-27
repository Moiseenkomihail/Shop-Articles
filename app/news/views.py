from django.shortcuts import render
from django.views.generic import CreateView,DetailView, ListView,UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin



from .models import *
# Create your views here.

class CreateNewsView(PermissionRequiredMixin, CreateView):
    permission_required = "news.add_news"
    model = News
    fields = ('title','photo')
    success_url = '/'
    template_name = 'news/createnews.html'

class ChangeNewsView(PermissionRequiredMixin, UpdateView):
    model = News
    permission_required = 'news.change_news'
    template_name = 'news/changenews'
    fields = [
        'title',
        'photo'
    ]
    success_url = '/'
