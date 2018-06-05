from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import auth

from .models import *

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
  
def question(request):
	question=Question.objects.all()
	return render_to_response("question.html",locals())
	
def home(request):
    return render_to_response("home.html",locals())

def post(request):
	if request.POST.get('max') > 0:
		if request.POST.get('max') == 1:
			return render(request, 'template2', context)
		elif request.POST.get('max') == 2:
			return render(request, 'template2', context)
		elif request.POST.get('max') == 3:
			return render(request, 'template2', context)
		elif request.POST.get('max') == 4:
			return render(request, 'template2', context)	
     
	#else:
    	#return render(request, "", {: })

# dragon
def wand(request):
	magic_Wand=Magic_Wand.objects.all()
	return render_to_response("wand.html",locals())

# dragon
def result(request):
	magic_Wand=Magic_Wand.objects.all()
	mahou_Shoujo=Mahou_Shoujo.objects.all()
	return render_to_response("result.html",locals())
