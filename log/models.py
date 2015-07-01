from django.db import models
from django.contrib import admin
# Create your models here.

class Log(models.Model):
	userip = models.IPAddressField()
    	logtime = models.CharField(max_length=32)
    	logcontext = models.CharField(max_length=32)
    	def __unicode__(self):
        	return self.userip

class LogAdmin(admin.ModelAdmin):
	list_display = ('userip','logtime','logcontext')
		
admin.site.register(Log, LogAdmin)