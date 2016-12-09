from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Article, Tag, Comment

class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'latest_article_list'

	def get_queryset(self):
		"""Return the last five published Articles."""
		return Article.objects.order_by('-pub_date')[:5]

class ArticleView(generic.DetailView):
	model = Article
	template_name = 'blog/article.html'

# Use non-generic views next time around
class TagView(generic.DetailView):
	model = Tag
	template_name = 'blog/tag.html'
	#context_object_name = 'tag_list'

	"""def get_queryset(self):
		return Tag.objects.order_by('pub_date')"""