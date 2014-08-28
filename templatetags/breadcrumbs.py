from django import template

from pages.models import Page


register = template.Library()


@register.inclusion_tag("breadcrumbs.html")
def breadcrumbs(path):
    parts = path.strip("/").split("/")
    crumbs = []
    # Ignore the "pages" part of the path: start at index 1.
    for i in range(1, len(parts)):
        url = "/" + "/".join(parts[0:i+1]) + "/"
        try:
            name = Page.objects.get(url=url).title
        except Page.DoesNotExist:
            name = parts[i]
            url = None
        if url == path:
            url = None
        crumbs.append({'name': name, 'url': url})
    return {'crumbs': crumbs}
