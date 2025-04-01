from django.contrib import admin

from .models import Article,Category,Comment,Message


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title','author','created','status')

    list_editable = ('status',)

    list_filter = ('status','created')



admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)