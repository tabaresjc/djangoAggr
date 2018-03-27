from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name='is_current_page')
def is_current_page(request, target):
    if not request or not target:
        return False

    view_name = request.resolver_match.view_name.replace('-paginated', '')

    return view_name == target

@register.filter(name='has_page')
def has_page(request, target):
    if not request or not target:
        return False

    view_name = request.resolver_match.view_name.replace('-paginated', '')

    return view_name in target
