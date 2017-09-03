from django import template
register = template.Library()

@register.filter
def replace_underscores(string):
    return string.replace('_', ' ')
