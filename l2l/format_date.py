from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='format_date')
def format_date(value):
    if isinstance(value, str):
        try:
            datetime_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
            return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            return value  
    return value