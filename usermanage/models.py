#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin

AUTH_CHOICES = (
    ('0','管理员'),
    ('1','普通用户'),
)

class User(models.Model):
	userip = models.IPAddressField(primary_key=True)
    	username = models.CharField(max_length=32)
    	password = models.CharField(max_length=32)
    	userauth = models.CharField(max_length=32)
    	userauth = models.CharField(u'权限',choices = AUTH_CHOICES,max_length = 32)
    	
    	def __unicode__(self):
        	return self.username

class UserAdmin(admin.ModelAdmin):
	list_display = ('userip','username','password','userauth')
		
admin.site.register(User, UserAdmin)