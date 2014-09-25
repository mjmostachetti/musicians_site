from django import forms
from django.forms import ModelForm, Textarea, CharField, TextInput, URLInput
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
		widgets = {
			'first_name': TextInput(attrs={
				'placeholder' : 'Enter your first name'
				}),
			'website' : URLInput(attrs={
				'value' : 'http://',
				}),
		}
		#add form "initial" for some of the stuff

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, initial="Insert the Purpose of Message")
	message = forms.CharField(widget=forms.Textarea, initial="Tell me more!")
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)