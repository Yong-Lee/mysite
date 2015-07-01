#coding=utf-8
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from configfile.models import DhcpMD5
from django.template import loader, Context
from forms import FwForm, DefaultForm, KsForm, addDhcpMD5Form, IPForm
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from mysite.CommonPaginator import SelfPaginator
import os,hashlib,types


def md5(str):
	import hashlib
	import types
	if type(str) is types.StringType:
	    	m = hashlib.md5()  
	    	m.update(str)
	    	return m.hexdigest()
	else:
    		return ''

def addmd5(fs,str):
	temp = fs.encode("utf-8") 
	dhcp = DhcpMD5()
	dhcp.username = str
	dhcp.dhcpmd5 = md5(temp)
	dhcp.save()


def shellshow(cmdstr):
    	result = os.popen(cmdstr)
    	res = result.read()
    	return res
    	# return HttpResponse(res)

@csrf_exempt
def dhcpconfig(request):
	username = request.session.get('username','')
	if username:
		if request.method == "POST":
			fw = FwForm(request.POST)
			if fw.is_valid():
				fs = request.POST.get('dhcpconfig')
				addmd5(fs,'dhcp')
				fi = open('/etc/dhcp/dhcpd.conf','w+')
				fi.write(fs)
				fi.close()
				temp = shellshow('service dhcpd start')
				print temp
				# shellshow('service dhcpd start')
				return render_to_response('dhcpconfig.html',{'dhcpconfig':fs,'username':username})
		else:
			fi = open('/etc/dhcp/dhcpd.conf','r+')
			str = ''
			for line in fi.readlines():
				str = str + line.lstrip()
			fi.close()
			# template = loader.get_template("configfile.html")
			# context = Context({'configfile':str,'username':name})
			# return HttpResponse(template.render(context))
			return render_to_response('dhcpconfig.html',{'dhcpconfig':str,'username':username})
		return render_to_response('dhcpconfig.html',{'dhcpconfig':fw.cleaned_data['dhcpconfig'],'username':username})
	else:
		return HttpResponseRedirect('/user/login/')


@csrf_exempt
def defaultconfig(request):
	username = request.session.get('username','')
	if username:
		try:
			if request.method == "POST":
				fw = DefaultForm(request.POST)
				if fw.is_valid():
					fs = request.POST.get('defaultconfig')
					addmd5(fs,'default')
					default = open('/tftpboot/pxelinux.cfg/default','w+')
					default.write(fs)
					default.close()
					# temp = shellshow('service dhcpd start')
					# print temp
					# shellshow('service dhcpd start')
					return render_to_response('defaultconfig.html',{'defaultconfig':fs,'username':username})
			else:
				default = open('/tftpboot/pxelinux.cfg/default','r+')
				str = ''
				for line in default.readlines():
					str = str + line
				default.close()
				# template = loader.get_template("configfile.html")
				# context = Context({'configfile':str,'username':name})
				# return HttpResponse(template.render(context))
				return render_to_response('defaultconfig.html',{'defaultconfig':str,'username':username})
			return render_to_response('defaultconfig.html',{'defaultconfig':fw.cleaned_data['defaultconfig'],'username':username})
		except IOError: 
    			print('IOError') 
    		finally: 
    			default.close() 
	else:
		return HttpResponseRedirect('/user/login/')


@csrf_exempt
def ksconfig(request):
	username = request.session.get('username','')
	if username:
		try:
			if request.method == "POST":
				fw = KsForm(request.POST)
				if fw.is_valid():
					fs = request.POST.get('ksconfig')
					addmd5(fs,'ks')
					ks = open('/home/pub/conf/ks.cfg','w+')
					ks.write(fs)
					ks.close()
					# temp = shellshow('service dhcpd start')
					# print temp
					# shellshow('service dhcpd start')
					return render_to_response('ksconfig.html',{'ksconfig':fs,'username':username})
			else:
				ks = open('/home/pub/conf/ks.cfg','r+')
				str = ''
				for line in ks.readlines():
					str = str + line
				ks.close()
				# template = loader.get_template("configfile.html")
				# context = Context({'configfile':str,'username':name})
				# return HttpResponse(template.render(context))
				return render_to_response('ksconfig.html',{'ksconfig':str,'username':username})
			return render_to_response('ksconfig.html',{'ksconfig':fw.cleaned_data['ksconfig'],'username':username})
		except IOError: 
    			print('IOError') 
    		finally: 
    			ks.close() 
	else:
		return HttpResponseRedirect('/user/login/')

def md5_all(request):
	username = request.session.get('username','')
	if username:
		md5_all = DhcpMD5.objects.all()
		lst = SelfPaginator(request,md5_all, 10)
		template = loader.get_template("md5.html")
		context = Context({'lPage':lst,'username':username})
		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect(reverse('login'))

def assignip(request):
	username = request.session.get('username','')
	if username:
		if request.method == "POST":
			ip = IPForm(request.POST)
			if ip.is_valid():
				iptemp = request.POST.get('assignip')
				str = 'ifconfig eth1.100 '+iptemp.encode("utf-8")+' netmask 255.255.255.0 up'
				shellshow('vconfig add eth1 100')
				shellshow(str)
		else:
			ip = IPForm()
	return render_to_response('assignip.html',{'ip':ip})