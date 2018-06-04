from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.home, name='home'),
	url(r'^result/$',views.result, name='result'),
	url(r'^wand/$',views.wand, name='wand'),
	url(r'^menu/$',views.menu, name='menu'),
	url(r'^question/$',views.index, name='question'),
]
