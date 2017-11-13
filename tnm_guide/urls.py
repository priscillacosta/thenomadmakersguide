from django.conf.urls import url
from django.contrib import admin
from tnm_guide import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
	url(r'^([0-9]+)/$', views.detail, name = 'detail'),
]

