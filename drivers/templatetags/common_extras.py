from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='is_member')
def is_member(user, group_name):
    return user.groups.filter(name=group_name).exists() or user.is_superuser