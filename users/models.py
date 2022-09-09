from django.db import models

# Create your models here.
class User(models.Model):
	first_name		= models.CharField(max_length=50, blank=False)
	last_name		= models.CharField(max_length=50, blank=False)
	complete_name	= ' '
	user_email		= models.EmailField(unique=True ,blank=False)
	isVerified		= models.BooleanField(default=False)