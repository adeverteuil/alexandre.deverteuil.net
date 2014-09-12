from django.contrib import admin

from images.models import Image, Collection


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    fields = ("title", "slug", "original", "collection")
    list_display = ("title", "collection", "slug")

admin.site.register(Collection)
