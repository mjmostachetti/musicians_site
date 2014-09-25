from django.shortcuts import render,redirect
from user.models import User
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from user.forms import UserForm
from django.shortcuts import render_to_response
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
			#user_ = User.objects.create()
			form.save()#for_user=user_)
			return HttpResponseRedirect('/profile/')
	else:
		form = UserForm()
	return render(request, 'new_user.html', {'form' : form})

def messages(request):
	return render(request, 'messages.html')

def about(request):
	return render(request, 'about.html')

def donate(request):
	return render(request, 'donate.html')

def splash(request):
	return render(request, 'splash.html')
	#login page

def search_city_state(request, user_state, user_city):
    users_in_city = User.objects.filter(
    	city = user_city,
    	state = user_state,
    )
    return HttpResponse(users_in_city)

def all_users(request):
	list_all = User.objects.all()
	output = ', '.join([p.city for p in list_all])
	return HttpResponse(output)

# search for users in the desired city and state
#def search_city_state(request, city, state):






