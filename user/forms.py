from django import forms
from django.forms import ModelForm
from user.models import User

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = [
			'first_name', 'last_name', 'instrument', 'email_address', 'bio',
			'website', 'link_to_music', 'city', 'country', 'state', 'zipcode', 
			'member_since'
		]