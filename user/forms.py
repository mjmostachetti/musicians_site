from django import forms
from django.forms import ModelForm
from user.models import User

class UserForm(ModelForm):
	
	#def save(self, for_user):
	#	self.instance.user = for_user
	#	return super().save()

	class Meta:
		model = User
		fields = [
			'first_name', 'last_name', 'instrument', 'email_address', 'bio',
			'website', 'link_to_music', 'city', 'country', 'state', 'zipcode',
			'birthday',
		]