from fileupload import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^fileupload/', views.fileupload, name='fileupload'),
	url(r'^osadd/',views.osadd,name='osadd'),
	url(r'^add/',views.add,name='add'),
	url(r'^osall/',views.os_all,name='osall'),
	url(r'^osdel/',views.osdel,name='osdel'),
	url(r'^pub/',views.pub,name='pub'),
)
