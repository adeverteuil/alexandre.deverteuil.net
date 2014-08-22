from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
