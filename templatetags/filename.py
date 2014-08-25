from django import template
from django.conf import settings

register = template.Library()

@register.filter
def filename(value):
    """Replace the string |filename| with the value of MEDIA_URL."""
    return value.replace("|filename|", settings.MEDIA_URL)
