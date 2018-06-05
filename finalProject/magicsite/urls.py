from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns=[
  	url(r'^$',views.index, name='index'),
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^register/$',views.register,name='register'),
	url(r'^result/$',views.result, name='result'),
	url(r'^wand/$',views.wand, name='wand'),
	url(r'^question/$',views.question, name='question'),
]