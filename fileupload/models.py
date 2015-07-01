from django.db import models
from django.contrib import admin
from usermanage.models import User
# Create your models here.

class OS(models.Model):
	userip = models.IPAddressField()
	# user = models.ForeignKey(usermanage.User)
	# user = models.ManyToManyField(User)
    	oscontext = models.CharField(max_length=32)
    	def __unicode__(self):
        	return self.user.userip

# class OSAdmin(admin.ModelAdmin):
# 	list_display = ('user.userip','oscontext')
		
# admin.site.register(OS, OSAdmin)