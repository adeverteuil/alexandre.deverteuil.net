from django.contrib import admin

from links.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):

    list_display = (
        "title", "url", "datetime_added", "datetime_modified", "private",
        )

admin.site.register(Bookmark, BookmarkAdmin)
