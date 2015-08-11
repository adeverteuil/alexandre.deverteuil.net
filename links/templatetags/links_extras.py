from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def tags_query_transform(context, **kwargs):
    updated = context['request'].GET.copy()
    for k, v in kwargs.items():
        if k == 'add':
            tags = updated.getlist('tag')
            if v not in tags:
                updated.appendlist('tag', v)
        if k == 'remove':
            tags = updated.pop('tag')
            if v in tags:
                tags.remove(v)
            updated.setlist('tag', tags)
    if updated.getlist('tag'):
        return "?" + updated.urlencode()
    else:
        return ""
