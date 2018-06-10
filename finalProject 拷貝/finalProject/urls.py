from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from magicsite import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^magicsite/',include('magicsite.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
