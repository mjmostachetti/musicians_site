from django.db import models

class User(models.Model):

	INSTRUMENT_CHOICES = (
		('Guitar', 'Guitar'),
		('Drums', 'Drums')
	)
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	instrument = models.CharField(max_length=30, choices=INSTRUMENT_CHOICES)
	email_address = models.CharField(max_length=70)
	bio = models.TextField()
	website = models.URLField(max_length=200)
	link_to_music = models.URLField(max_length=100)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zipcode = models.PositiveIntegerField(null=True)
	birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)

	#member_since = models.DateField(auto_now_add=True)
	#picture = models.ImageField(height_field=) figure this out!!!!
	#age = models.IntegerField()
	#genra_looking_for = models.dropdown list?


class Instrument(models.Model):
	pass
	#each user has an instrument
	# add make - model 