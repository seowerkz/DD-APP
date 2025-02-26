from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='is_exclusive_member')
def is_exclusive_member(user, group_name):
    return user.groups.filter(name=group_name).exists()