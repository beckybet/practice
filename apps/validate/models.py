from __future__ import unicode_literals

from django.db import models
import re 

emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



#managers have functions in your models 

class validEmailManager(models.Manager):
	#use Regex string at the beginning of the assignment so you can grab it from the website 
	def emailcheck(self, email): 
		if emailRegex.math(email):
			Email.objects.create(email=email)

# Create your models here.
class Email(models.Model):
	email = models.CharField(max_length=10) 
	created_at = models.DateTimeField(auto_now_add=True) 
	updated_at = models.DateTimeField(auto_now_add=True) 
	objects= validEmailManager()


	#most of the time you do min length on emails so that you get emails that fake? there's not validation
	