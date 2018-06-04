<<<<<<< HEAD
from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.home, name='home'),
	url(r'^result/$',views.result, name='result'),
	url(r'^wand/$',views.wand, name='wand'),
	url(r'^menu/$',views.menu, name='menu'),
	url(r'^question/$',views.index, name='question'),
]
=======
from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index, name='index'),
	url(r'^result/$',views.result, name='result'),# dragon
	url(r'^wand/$',views.wand, name='wand'),# dragon
]
>>>>>>> 2af5f2693af9c831a797a5007cb46fcfd06abede
