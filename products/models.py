from django.db import models
import os

class Product(models.Model):
	title 		= models.CharField(max_length=120)	# Name of the product - Can't be blank
	price 		= models.DecimalField(decimal_places=2, max_digits=9)
	description = models.TextField(blank=True, null=True)	# blank=True == not required in case of field, null=True == not a required field in case of db
	ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
	image		= models.ImageField(upload_to="static/", default="images/unavailable-image.jpg", null=True)

