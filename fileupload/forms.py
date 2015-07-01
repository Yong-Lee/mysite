#coding:utf-8
from django import forms
from fileupload.models import OS

class FileForm(forms.Form):
	# fileName = forms.CharField()
	filepath = forms.FileField()

class SystemForm(forms.ModelForm):
	userip = forms.IPAddressField(
	        	label = u"用户IP",
	        	error_messages = {'required':u'请输入用户IP'},
	    	)
	oscontext = forms.CharField(
        	label = u"操作系统名称",
        	error_messages = {'required':u'请输入操作系统名称'},
        	widget = forms.TextInput(attrs={
                	'size':'32',
            	}
        	)
    	)
	class Meta:
		model = OS