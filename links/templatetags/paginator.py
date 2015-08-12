from django import template

register = template.Library()

def paginator(context, adjacent_pages=5):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    page_num = context['page_obj'].number
    num_pages = context['paginator'].num_pages
    lower_pages = page_num - 1
    higher_pages = num_pages - page_num
    extra_right = max(adjacent_pages - lower_pages, 0)
    extra_left = max(adjacent_pages - higher_pages, 0)
    start = max(page_num - adjacent_pages - extra_left, 1)
    end = min(page_num + adjacent_pages + extra_right, num_pages)
    page_range = list(range(start, end+1))

    context['page_range'] = page_range
    context['show_first'] = 1 not in page_range
    context['show_last'] = num_pages not in page_range
    return context

register.inclusion_tag('links/_paginator.html', takes_context=True)(paginator)
