from django.contrib import admin

from images.models import Image, Collection


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    fields = (
        "title",
        "basename",
        "original",
        "collection",
        )
    list_display = (
        "title",
        "collection",
        "basename",
        "original_width",
        "original_height",
        )

admin.site.register(Collection)
