from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *

def index(request):
	question=Question.objects.all()
	return render_to_response("index.html",locals())
	
def home(request):
<<<<<<< HEAD
    return render_to_response("home.html",locals())
	
=======
    return render(request, 'home.html')
>>>>>>> 2af5f2693af9c831a797a5007cb46fcfd06abede

# dragon
def wand(request):
	magic_Wand=Magic_Wand.objects.all()
	return render_to_response("wand.html",locals())

# dragon
def result(request):
	magic_Wand=Magic_Wand.objects.all()
	mahou_Shoujo=Mahou_Shoujo.objects.all()
	return render_to_response("result.html",locals())