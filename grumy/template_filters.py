from google.appengine.ext import webapp
import random

register = webapp.template.create_template_register()

@register.filter
def choice(choices):
    return random.choice(choices)