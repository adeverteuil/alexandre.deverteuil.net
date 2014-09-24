from django.contrib import admin

from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    fields = (
        "original",
        )
    list_display = (
        "original",
        "original_width",
        "original_height",
        )
