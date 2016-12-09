from django.contrib import admin

# Register your models here.
from .models import Article, Tag, Comment

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

class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'poster', 'pub_date')

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'created_date', 'last_edit_date')
    exclude = ('tags', )
    inlines = (
       TagInline, CommentInline
    )


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)