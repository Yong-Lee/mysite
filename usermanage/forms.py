#coding:utf-8
from django import forms
from usermanage.models import User,AUTH_CHOICES

class LoginForm(forms.Form):
  userip = forms.IPAddressField(
            label = u"用户IP",
            error_messages = {'required':u'请输入用户IP'},
        )
  username = forms.CharField(
          label = u"用户名",
          error_messages = {'required':u'请输入用户名'},
          widget = forms.TextInput(attrs={
                  'size':'32',
              }
          )
      )
  password = forms.CharField(
          label = u"密码",
          error_messages = {'required':u'请输入密码'},
          widget = forms.PasswordInput(
            attrs = {
                'size':'32',
            }
        ),
      )
  userauth = forms.ChoiceField(required=True,choices=AUTH_CHOICES,label=u"权限")

class UserForm(forms.ModelForm):
	userip = forms.IPAddressField(
	        	label = u"用户IP",
	        	error_messages = {'required':u'请输入用户IP'},
	    	)
	username = forms.CharField(
        	label = u"用户名",
        	error_messages = {'required':u'请输入用户名'},
        	widget = forms.TextInput(attrs={
                	'size':'32',
            	}
        	)
    	)
	password = forms.CharField(
        	label = u"密码",
        	error_messages = {'required':u'请输入密码'},
        	widget = forms.PasswordInput(
           	attrs = {
              	'size':'32',
           	}
       	),
    	)
	userauth = forms.ChoiceField(required=True,choices=AUTH_CHOICES,label=u"权限")
	class Meta:
		model = User

class UpdateUserForm(forms.ModelForm):
	username = forms.CharField(
        	label = u"用户名",
        	error_messages = {'required':u'请输入用户名'},
        	widget = forms.TextInput(attrs={
                	'size':'32',
            	}
        	)
    	)
	password = forms.CharField(
        	label = u"密码",
        	error_messages = {'required':u'请输入密码'},
        	widget = forms.PasswordInput(
           	attrs = {
              	'size':'32',
           	}
       	),
    	)
	userauth = forms.ChoiceField(required=True,choices=AUTH_CHOICES,label=u"权限")
	class Meta:
		model = User
		fields = ('username','password','userauth')