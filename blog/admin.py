from django.contrib import admin
from blog.models import Post, Category


def make_public(modeladmin, request, queryset):
    queryset.update(public=True)
make_public.short_description = "Mark as public"

def make_not_public(modeladmin, request, queryset):
    queryset.update(public=False)
make_not_public.short_description = "Mark as private"


class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "summary", "format_date", "public")
    list_editable = ("summary", "public")
    fields = (
        ("title", "pub_date"),
        ("slug", "public"),
        "summary",
        "body",
        "categories",
        )
    ordering = ("-pub_date",)
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_public, make_not_public]
    date_hierarchy = "pub_date"

    # Represent dates in yyyy-mm-dd hh:mm format on the admin list display.
    # source:  https://docs.djangoproject.com/en/1.6/topics/i18n/
    def format_date(self, obj):
        return obj.pub_date.strftime("%Y-%m-%d %H:%M")
    format_date.short_description = "Date published"
    format_date.admin_order_field = "pub_date"

    class Media:
        css = {
            'all': ("admin/css/site.css",),
            }


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
