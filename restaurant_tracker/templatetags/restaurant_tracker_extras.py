from django import template
import locale

#locale.setlocale(locale.LC_ALL, '')

register = template.Library()

@register.filter
def get_range(min_val, max_val):
    """
    Returns a range of values
    """
    return range(min_val, max_val)

@register.filter
def string_or_default(message, default_message):
    """
    Returns a given string, or a default message if the string is empty or invalid
    """
    if (message is None or (not isinstance(message, str)) or len(message) < 1):
        return default_message
    else:
        return message

@register.filter()
def currency(value):
    """
    Returns a string currency representation of a float
    """
    return '${:,.2f}'.format(value)#locale.currency(value, grouping=True)