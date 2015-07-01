#coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from usermanage.models import User
from django.template import loader, Context
from forms import UserForm,UpdateUserForm,LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from log.views import addlog
from mysite.CommonPaginator import SelfPaginator

def register(request):
    	if request.method == "POST":
	    	uf = UserForm(request.POST)
	    	if uf.is_valid():
	    		userip = request.POST.get('userip')
	    		username = request.POST.get('username')
	    		password = request.POST.get('password')
	        	userauth = request.POST.get('userauth')
	        	user = User()
	        	user.userip = userip
	        	user.username = username
	        	user.password = password
	        	user.userauth = userauth
	        	user.save()

	        	return HttpResponseRedirect(reverse('login'))
    	else:
        	uf = UserForm()
    	return render_to_response('register.html',{'uf':uf})

def user(request):
		username = request.session.get('username','')
		userauth = request.session.get('userauth',u'1')
		if username and userauth==u'0':
			user_all = User.objects.all()
			lst = SelfPaginator(request,user_all, 10)
			template = loader.get_template("usermanage.html")
			context = Context({'username':username,'lPage':lst})
			return HttpResponse(template.render(context))
		else:
			return HttpResponseRedirect(reverse('login'))

# @csrf_exempt
def login(request):
    	if request.method == "POST":
	    	uf = LoginForm(request.POST)
	    	if uf.is_valid():
	    		userip = request.POST.get('userip')
	    		username = request.POST.get('username')
	    		password = request.POST.get('password')
	    		userauth = request.POST.get('userauth')

		    	user = User.objects.filter(userip__exact = userip,username__exact = username,password__exact = password,userauth__exact = userauth)
		    	if user and userauth==u'0':
		    		request.session['userip'] = userip
		    		request.session['username'] = username
		    		request.session['userauth'] = userauth
		    		request.session.set_expiry(0)
		    		addlog(request.session.get('userip',''),'管理员用户登录')
		    		return HttpResponseRedirect(reverse('usermanage'))
		    	elif user:
		    		request.session['username'] = username
		    		request.session['userauth'] = userauth
		    		request.session.set_expiry(0)
		    		addlog(request.session.get('userip',''),'普通用户登录')
		    		return HttpResponseRedirect(reverse('pub'))
		    	else:
		    		addlog(request.session.get('userip',''),'用户登录失败')
		    		return render_to_response('login.html',{'uf':uf})
    	else:
    		uf = LoginForm()
    	return render_to_response('login.html',{'uf':uf})

def logout(request):
    	del request.session['username']
    	addlog(request.session.get('userip',''),'用户注销')
    	return HttpResponseRedirect(reverse('login'))

def userupdate(request):
	username = request.session.get('username','')
	userauth = request.session.get('userauth',u'1')
	if username and userauth==u'0':
	    	ip = request.GET['userip']
	    	uf = UpdateUserForm()
	  	return render_to_response('update.html',{'uf':uf,'userip':ip,'username':username})
	else:
		return HttpResponseRedirect(reverse('login'))



def update(request):
	userip = request.POST['userip']
	if request.method == 'POST':
	    	uf = UpdateUserForm(request.POST)
	    	if uf.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			userauth = request.POST['userauth']
			user = User.objects.get(userip=userip)
			if user:
				user.username = username
				user.password = password
				user.userauth = userauth
				user.save()
				addlog(request.session.get('userip',''),'用户更新')
				return HttpResponseRedirect(reverse('usermanage'))
			else:
				addlog(request.session.get('userip',''),'数据库没有该用户')
				return render_to_response('update.html',{'uf':uf,'userip':ip,'username':username})
	else:
        	uf = UpdateUserForm()
        	addlog(request.session.get('userip',''),'用户更新失败')
        	return HttpResponseRedirect(reverse('usermanage'))
    	return render_to_response('update.html',{'uf':uf})

def useradd(request):
	username = request.session.get('username','')
	uf = UserForm()
  	return render_to_response('useradd.html',{'uf':uf,'username':username})

def add(request):
	if request.method == "POST":
	    	uf = UserForm(request.POST)
	    	if uf.is_valid():
			userip = request.POST['userip']
			name = request.POST['username']
			pwd = request.POST['password']
			auth = request.POST['userauth']
			user = User()
			user.userip = userip
			user.username = name
			user.password = pwd
			user.userauth = auth
			user.save()
			addlog(request.session.get('userip',''),'用户添加')
			return HttpResponseRedirect(reverse('usermanage'))
	else:
        	uf = UserForm()
        	addlog(request.session.get('userip',''),'用户添加失败')
    	return render_to_response('useradd.html',{'uf':uf})


def delete(request):
	userip = request.GET['userip']
	user = User.objects.get(userip=userip)
	user.delete()
	addlog(request.session.get('userip',''),'用户删除')
	return HttpResponseRedirect(reverse('usermanage'))
