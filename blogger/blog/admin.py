from django.contrib import admin

# Register your models here.
from .models import Article, Tag

"""class TagInline(admin.TabularInline):
    model = Tag.articles.through
    extra = 3"""

"""class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'pub_date']
    list_display = ('title', 'pub_date', 'created_date', 'last_edit_date')
    #inlines = [TagInline]
    filter_horizontal = ('tags',)"""



class TagInline(admin.TabularInline):
    model = Article.tags.through


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('tags', )
    inlines = (
       TagInline,
    )


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)