from django.contrib import admin
from django.template.defaultfilters import title

from .models import Article,Category,Comment,Message


class FilterByTitle(admin.SimpleListFilter):

    title = 'عنوان مقاله'
    parameter_name = 'title'
    def lookups(self, request, model_admin):
        return (
            ('eagle','eagle'),
            ('solar','solar'),
            ('css','css'),
        )
    def queryset(self, request, queryset):

        if self.value():

            return queryset.filter(title__icontains=self.value())


class CommentInLine(admin.TabularInline):

    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title','created','show_image','status',)

    list_editable = ('status',)

    list_filter = ('status',FilterByTitle)

    search_fields = ('title','body')

    inlines = (CommentInLine,)

    fields = ('title','body','category','image','status')




admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)