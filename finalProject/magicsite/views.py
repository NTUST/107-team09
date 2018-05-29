from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *
# Create your views here.
def index(request):
	question_sets=Question_Set.objects.all()
	return render_to_response("magicsite/menu.html",locals())
	
def home(request):
    return render(request, 'magicsite/home.html')