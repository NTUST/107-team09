from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import *
# Create your views here.
def index(request):
	question_sets=Question_Set.objects.all()
	return render_to_response("magicsite/menu.html",locals())