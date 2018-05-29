from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
	question=Question.objects.all()
	return render_to_response('index.html', locals())