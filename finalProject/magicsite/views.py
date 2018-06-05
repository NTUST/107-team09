from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from .models import *

def index(request):
	return render(request, 'index.html')

def home(request):
  return render(request, 'home.html')
    
def menu(request):
	question_sets=Question_Set.objects.all()
  return render(request, 'menu.html')


def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		repassword = request.POST.get('repassword')
		if password == repassword:
			check_user = User.objects.filter(username=username)
			if len(check_user) == 0:
				user = User.objects.create_user(username, '', password)
				user.backend = 'django.contrib.auth.backends.ModelBackend'
				auth.login(request, user)
				return redirect('/magicsite/')
			else: return HttpResponse("<script>alert('使用者名稱重複');window.location = '/magicsite/register/';</script>")
		else: return HttpResponse("<script>alert('密碼與確認密碼不同');window.location = '/magicsite/register/';</script>")
		form = UserCreationForm(request.POST)
	return render(request,'register.html')

def login(request):
	if not request.user.is_authenticated(): 
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/magicsite/')
		else: return render(request, 'login.html', {})
	else: return redirect('/magicsite/')

def logout(request):
	auth.logout(request)
	return redirect('/magicsite/')


def question(request):
	question = Question.objects.all()
	return render(request, "question.html", {'question': question})

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

def wand(request):
	magic_Wand = Magic_Wand.objects.all()
	return render(request, "wand.html", {'magic_Wand': magic_Wand})

def result(request):
	magic_Wand = Magic_Wand.objects.all()
	mahou_Shoujo = Mahou_Shoujo.objects.all()
	return render(request, "result.html", 
		{
			'magic_Wand': magic_Wand,
			'mahou_Shoujo': mahou_Shoujo
		}
	)
