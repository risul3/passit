from django.contrib import admin

from .models import Post, Tag

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("post_title",)}		

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)