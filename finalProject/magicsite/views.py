from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *

def index(request):
	question=Question.objects.all()
	return render_to_response("index.html",locals())
	
def home(request):
    return render(request, 'magicsite/home.html')
