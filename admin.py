from django.contrib import admin
from blog.models import Post, Category


def make_public(modeladmin, request, queryset):
    queryset.update(public=True)
make_public.short_description = "Mark as public"

def make_not_public(modeladmin, request, queryset):
    queryset.update(public=False)
make_not_public.short_description = "Mark as private"


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "pub_date", "public")
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_public, make_not_public]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
