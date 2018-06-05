from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *

def index(request):
	question=Question.objects.all()
	return render_to_response("index.html",locals())
	
def home(request):
    return render_to_response("home.html",locals())
    
def menu(request):
	question_sets=Question_Set.objects.all()
	return render_to_response("menu.html",locals())

def wand(request):
	magic_Wand=Magic_Wand.objects.all()
	return render_to_response("wand.html",locals())

def result(request):
	magic_Wand=Magic_Wand.objects.all()
	mahou_Shoujo=Mahou_Shoujo.objects.all()
	return render_to_response("result.html",locals())