from django import template

register = template.Library()

@register.filter
def get_range(min, max):
    """Returns a range of values"""
    return range(min,max)