from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import auth

from .models import *
# Create your views here.
def index(request):
	return render_to_response('index.html',locals())

def home(request):
	return render(request, 'magicsite/home.html')

def login(request):
	if request.user.is_authenticated(): 
		 return HttpResponseRedirect('/index/')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/magicsite/index/')
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/magicsite/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/magicsite/index/')
    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form': form})