from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def query_transform(context, *args):
    query = context['request'].GET.copy()
    for arg in args:
        k, v = arg.split("=")
        if k.startswith("+"):
            k = k.strip("+")
            l = query.getlist(k)
            if v not in l:
                query.appendlist(k, v)
        elif k.startswith("-"):
            k = k.strip("-")
            l = query.pop(k)
            if v in l:
                l.remove(v)
            query.setlist(k, l)
        else:
            query.set(k, v)
    return "?" + query.urlencode() if query else ""
