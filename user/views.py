from django.shortcuts import render,redirect
from user.models import User
from django.http import HttpResponse, HttpResponseRedirect
from user.forms import UserForm
import datetime


def home_page(request):
	#response = HttpResponse("This is my response")
	return render(request, 'home.html')
	#render(request, 'home.html')

def profile(request):
	return render(request, 'profile.html')

def map(request):
	return render(request, 'map.html')

def new_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/profile/')
	else:
		form = UserForm()

	return render(request, 'new_user.html', {'form' : form})

def messages(request):
	return render(request, 'messages.html')

def about(request):
	return render(request, 'about.html')


