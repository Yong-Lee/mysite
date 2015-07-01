from django.db import models
from django.contrib import admin

class DhcpMD5(models.Model):
	username = models.IPAddressField()
    	dhcpmd5 = models.CharField(max_length=32)
    	def __unicode__(self):
        	return self.dhcpmd5

class DhcpMD5Admin(admin.ModelAdmin):
	list_display = ('username','dhcpmd5')
		
admin.site.register(DhcpMD5, DhcpMD5Admin)