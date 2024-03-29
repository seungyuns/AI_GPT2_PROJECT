from django.db import models

class Blog(models.Model):
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	body = models.TextField()
	
	def __str__(self):
		return self.title
	
	def summary(self):
		return self.body[:100]
