from usermanage import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^login/', views.login, name='login'),
	url(r'^usermanage/', views.user, name='usermanage'),
	url(r'^register/', views.register, name='register'),
	url(r'^logout/',views.logout),
	url(r'^userupdate/',views.userupdate),
	url(r'^update/',views.update,name='update'),
	url(r'^add/',views.add),
	url(r'^delete/',views.delete),
	url(r'^useradd/',views.useradd),
)
