from configfile import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^dhcpconfig/', views.dhcpconfig, name='dhcpconfig'),
	url(r'^defaultconfig/', views.defaultconfig, name='defaultconfig'),
	url(r'^ksconfig/',views.ksconfig,name='ksconfig'),
	url(r'^md5/',views.md5_all,name='md5'),
	url(r'^assignip/',views.assignip,name='assignip'),
)
