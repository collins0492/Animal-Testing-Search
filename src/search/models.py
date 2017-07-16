from django.db import models
import datetime

class Tester(models.Model):
	company = models.CharField(max_length = 500)
	parent = models.CharField(max_length = 500, null = True, blank = True)
	status = models.BooleanField(default = 0)
	updated = models.DateTimeField(default = datetime.datetime.now(), blank = True)

	def __str__(self):
		return self.company






#'''''''''''''''
#Run after making changes to this file
#--------------------------------------
#python manage.py makemigrations
#python manage.py migrate