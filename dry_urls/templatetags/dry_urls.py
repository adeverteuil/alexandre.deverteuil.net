import re

from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter
def dry_urls(text):
    """Parse |media_url|, |static_url| and |url ...| in the input text."""
    text = text.replace("|media_url|", settings.MEDIA_URL)
    text = text.replace("|static_url|", settings.STATIC_URL)
    # |url ...| has the same syntax as {% url %}.
    text = re.sub("\| *url *([^|]+) *\|", reverse_url, text)
    return text


def reverse_url(match):
    text = match.group(1)
    t= template.Template("{% url " + text + " %}")
    context = template.Context()
    return t.render(context)
