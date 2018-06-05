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