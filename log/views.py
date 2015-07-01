#coding=utf-8
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from log.models import Log
from django.template import loader, Context
from forms import LogForm, SelectLogForm
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from mysite.CommonPaginator import SelfPaginator
# Create your views here.

def log_all(request):
	username = request.session.get('username','')
	if username:
		log_all = Log.objects.all()
		lst = SelfPaginator(request,log_all, 10)
		template = loader.get_template("log.html")
		context = Context({'lPage':lst,'username':username})
		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect(reverse('login'))


def addlog(userip,logcontext):
	import time
	log = Log()
	logtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	log.userip = userip
	log.logtime = logtime
	log.logcontext = logcontext
	log.save()
	return HttpResponseRedirect(reverse('log'))

def selectlog(request):
	username = request.session.get('username','')
	if username:
		if request.method == "POST":
    			userip = request.POST.get('selectip')
    			print userip
			# log_all = Log.objects.all().extra(select={})
			log_all = Log.objects.filter(userip=userip)
			lst = SelfPaginator(request,log_all, 10)
			template = loader.get_template("log.html")
			context = Context({'lPage':lst,'username':username})
			# context = Context({'lPage':lst,'username':username,'userip':userip})
			return HttpResponse(template.render(context))
    		return HttpResponseRedirect(reverse('log'))
	else:
		slf = SelectLogForm()
		return render_to_response('log.html',{'slf':slf})
