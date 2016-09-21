from django.shortcuts import render, redirect
from .models import Email 
from django.contrib import messages 

def index(request):
	return render(request, "app1/index.html")


def validate(request):
	#you want to define an email that shows that you did something successfully 
	email = request.POST['email']
	isValid = email.EmailManager.emailCheck(email)
	if isValid:
		#this is where you want to set messages. you will have to print this to the client if this is true or false. this is where 
		#we will set messages 
		#there are different types of messages that you can use. every one can use something different 
		# custom messages please go back to it at some point 
		#we are going to use success and we are going to use errors 
		messages.add_message(request, messages.INFO, 'Hello world.')
		messages.success(request, 'The email address you entered ({}) is valid'.format(email))
		return redirect(request,"/success")
	else:
		messages.error(request, "The email address you entered({}). is invalid".format(email))
		return redirect('/')
	
#always try to break your code so that its always doing one thing at a time 

def success(request):
	#you want to define an email that shows that you did something successfully 
	context={'emails' : Email.objects.all() }
	return render(request, "validate/success.html", context)
	pass
