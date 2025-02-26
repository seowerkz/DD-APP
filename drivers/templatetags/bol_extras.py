from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='convert_date')
def convert_date(value):
    if type(value) is datetime:
        return value.strftime('%d %B %Y - %H:%M')
    return value