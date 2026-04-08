from django.contrib import admin

from .models import BlogPost

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
    )

admin.site.register(BlogPost, PostAdmin)
