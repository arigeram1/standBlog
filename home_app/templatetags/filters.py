import datetime
from datetime import timezone

from django import template


register = template.Library()

@register.filter
def cutter(value,arg):
    return value[:arg]



