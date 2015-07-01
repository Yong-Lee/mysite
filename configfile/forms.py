from django import forms
from configfile.models import DhcpMD5
# from usermanage.models import User

class FwForm(forms.Form):
	dhcpconfig = forms.CharField(max_length=10000)

class DefaultForm(forms.Form):
	defaultconfig = forms.CharField(max_length=10000)

class KsForm(forms.Form):
	ksconfig = forms.CharField(max_length=10000)

class addDhcpMD5Form(object):
	class Meta:
		model = DhcpMD5

class IPForm(forms.Form):
	assignip = forms.IPAddressField()