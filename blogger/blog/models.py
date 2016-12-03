from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	created_date = models.DateTimeField('date created', auto_now_add=True)
	last_edit_date = models.DateTimeField('date last edited', auto_now=True)