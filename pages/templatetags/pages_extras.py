from django import template
from pages.models import Page

register = template.Library() # Registering the template library

@register.simple_tag # This tag retrieves all Page objects
def get_all_pages():
    pages = Page.objects.all()
    return pages