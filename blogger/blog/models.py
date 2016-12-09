from django.db import models

# Create your models here.
class Tag(models.Model):
	#article = models.ForeignKey(Article, on_delete=models.CASCADE)
	tag_text = models.CharField(max_length=50)
	def __str__(self):
		return self.tag_text

class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	created_date = models.DateTimeField('date created', auto_now_add=True)
	last_edit_date = models.DateTimeField('date last edited', auto_now=True)
	tags = models.ManyToManyField(Tag)
	def __str__(self):
		return self.title

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	poster = models.CharField(max_length=20)
	body = models.TextField()
	pub_date = models.DateTimeField('date posted', auto_now_add=True)
	def __str__(self):
		return self.body[:100]
