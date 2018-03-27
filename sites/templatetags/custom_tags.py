from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(name='pagination_link')
def pagination_link(value, page, params=None):
    if not params:
        params = ()

    params = params + (page,)
    if 'paginated' not in value:
        value = '%s-paginated' % value

    return reverse(value, args=params)
