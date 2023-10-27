from django.shortcuts import render, redirect
from .forms import *
from news.models import News
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# calss HomeView()

def homepage(request):
    news = News.objects.all().order_by('-id')[:6]

    return render(request, 'basicpages/homepage.html', {'title':'Home', 'news':news})

def about(request):
    return render(request, 'basicpages/about.html', {'title':'About'})

def sign_up(request):
    if request.method == 'GET':
        form = RegistrateForm()
        return render(request, 'basicpages/signup.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegistrateForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'basicpages/signup.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return redirect('home')

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'basicpages/login.html', {'form':form, 'title':'log in'})

@login_required
def user_profile(request):
    return render(request, 'basicpages/userprofile.html')
