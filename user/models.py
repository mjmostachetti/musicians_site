from django.db import models

class User(models.Model):
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	instrument = models.CharField(max_length=30)
	email_address = models.CharField(max_length=70)
	bio = models.TextField()
	website = models.CharField(max_length=100)
	link_to_music = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zipcode = models.IntegerField(null=True)

	member_since = models.DateField(auto_now_add=True)
	#picture = models.ImageField(height_field=) figure this out!!!!
	#age = models.IntegerField()
	#genra_looking_for = models.dropdown list?





