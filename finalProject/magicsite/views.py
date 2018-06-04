from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *

def index(request):
	question=Question.objects.all()
	return render_to_response("index.html",locals())
	
def home(request):
    return render(request, 'home.html')
    
def index(request):
	question_sets=Question_Set.objects.all()
	return render_to_response("result.html",locals())
	

# dragon
def wand(request):
	magic_Wand=Magic_Wand.objects.all()
	return render_to_response("wand.html",locals())

# dragon
def result(request):
	magic_Wand=Magic_Wand.objects.all()
	mahou_Shoujo=Mahou_Shoujo.objects.all()
	return render_to_response("result.html",locals())