from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from pages.models import Page

class PageAdmin(FlatPageAdmin):

    # Add the description and pub_date fields.
    FlatPageAdmin.fieldsets[0][1]['fields'] = (
        'url', 'title', 'description', 'content', ('sites', 'pub_date')
        )
    list_display = ("url", "title", "description", "pub_date")

    class Media:
        css = {
            'all': ("admin/css/site.css",),
            }

admin.site.unregister(FlatPage)
admin.site.register(Page, PageAdmin)
