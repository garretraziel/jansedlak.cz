from django.contrib import admin
from blog.models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    fields = ("published", "title", "content", "tags")
    list_display = ["published", "title", "date_published", "author"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "author", "tags", "date_published"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)