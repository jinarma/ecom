from django.db import models
import pyotp
# Create your models here.
class PhoneModel(models.Model):
	mobile		= models.IntegerField(blank=False, max_length=10)
	isVerified	= models.BooleanField(blank=False, default=False)
