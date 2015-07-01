from log import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^log/', views.log_all, name='log'),
	url(r'^selectlog/',views.selectlog,name='selectlog'),
)
