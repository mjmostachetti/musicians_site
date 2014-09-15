from django.shortcuts import render,redirect
from user.models import User
from django.http import HttpResponse
import datetime

def home_page(request):
	#response = HttpResponse("This is my response")
	return render(request, 'home.html')
	#render(request, 'home.html')

# Create your views here.
