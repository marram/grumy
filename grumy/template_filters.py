from google.appengine.ext import webapp
import random
from django.utils.safestring import mark_safe, SafeData, mark_for_escaping
register = webapp.template.create_template_register()


@register.filter
def choice(choices):
    return random.choice(choices)

@register.filter
def safe(value):
    """
    Marks the value as a string that should not be auto-escaped.
    """
    return mark_safe(value)