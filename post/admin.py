from django.contrib import admin

from .models import Post, Tag

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("post_title",)}
	list_display = ('post_title', 'get_tags', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)