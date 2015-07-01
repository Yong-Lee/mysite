#coding=utf-8
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from fileupload.models import OS
from django.template import loader, Context
# from django import forms
from forms import FileForm
from forms import SystemForm
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from configfile.views import addmd5
from mysite.CommonPaginator import SelfPaginator

# class FileForm(forms.Form):
# 	# fileName = forms.CharField()
# 	filepath = forms.FileField()

@csrf_exempt
def fileupload(request):
	username = request.session.get('username','')
	if username:
		if request.method == "POST":
			isofile = FileForm(request.POST, request.FILES)
			if isofile.is_valid():
				fp = file('/upload/'+isofile.cleaned_data['filepath'].name,'wb')
				s = isofile.cleaned_data['filepath'].read()
				addmd5(s,'fileupload')
				fp.write(s)
				fp.close()
				return render_to_response('fileok.html',{'isofile':isofile.cleaned_data['filepath'].name,'username':username})
		else :
			isofile = FileForm()
		return render_to_response('fileupload.html',{'isofile':isofile,'username':username})
	else:
		return HttpResponseRedirect('/user/login/')

def os_all(request):
		username = request.session.get('username','')
		userauth = request.session.get('userauth',u'1')
		if username and userauth==u'0':
			os_all = OS.objects.all()
			lst = SelfPaginator(request,os_all, 10)
			template = loader.get_template("osall.html")
			context = Context({'lPage':lst,'username':username})
			return HttpResponse(template.render(context))
		else:
			return HttpResponseRedirect(reverse('login'))

def pub(request):
		userip = request.session.get('userip','')
		username = request.session.get('username','')
		userauth = request.session.get('userauth',u'1')
		if username and userauth==u'1':
			# userip = request.GET['userip']
			userip = userip.encode("utf-8")
			# print userip
			os_all = OS.objects.all()
			lst = SelfPaginator(request,os_all, 10)
			template = loader.get_template("pub.html")
			context = Context({'lPage':lst,'username':username,'userip':userip})
			return HttpResponse(template.render(context))
		else:
			return HttpResponseRedirect(reverse('login'))

# def addOS(userip,oscontext):
# 	os = OS()
# 	os.userip = userip
# 	os.oscontext = oscontext
# 	os.save()
# 	return HttpResponseRedirect(reverse('os'))

def osadd(request):
	username = request.session.get('username','')
	of = SystemForm()
	return render_to_response('osadd.html',{'of':of,'username':username})

def add(request):
	if request.method == "POST":
	    	of = SystemForm(request.POST)
	    	if of.is_valid():
			userip = request.POST['userip']
			oscontext = request.POST['oscontext']
			os = OS()
			os.userip = userip
			os.oscontext = oscontext
			os.save()
			return HttpResponseRedirect(reverse('fileupload'))
	else:
        	of = SystemForm()
    	return render_to_response('osadd.html',{'of':of})

def osdel(request):
	id = request.GET['id']
	os = OS.objects.get(id = id)
	os.delete()
	return HttpResponseRedirect(reverse('osall'))