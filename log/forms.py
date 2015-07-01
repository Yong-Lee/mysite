#coding:utf-8
from django import forms
from log.models import Log

class LogForm(forms.ModelForm):
	class Meta:
		model = Log


class SelectLogForm(forms.ModelForm):
	userip = forms.IPAddressField(
	        	label = u"用户IP",
	        	error_messages = {'required':u'请输入用户IP'},
	    	)
	# logcontext = forms.CharField(
 #        	label = u"日志内容",
 #        	error_messages = {'required':u'请输入日志内容'},
 #        	widget = forms.TextInput(attrs={
 #                	'size':'32',
 #            	}
 #        	)
 #    	)
	class Meta:
		model = Log
		fields = ('userip',)