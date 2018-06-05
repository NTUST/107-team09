from django.conf.urls import url

from django.contrib.auth.views import login, logout
from . import views

urlpatterns=[
	url(r'^result/$',views.result, name='result'),
	url(r'^wand/$',views.wand, name='wand'),
	url(r'^menu/$',views.menu, name='menu'),
	url(r'^question/$',views.question, name='question'),
]
