from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'pub_date']
    list_display = ('title', 'pub_date', 'created_date', 'last_edit_date')

admin.site.register(Article, ArticleAdmin)