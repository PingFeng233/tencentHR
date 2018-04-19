from django import template
from ..models import Category,WorkLocation
from django.db.models import Count

# register = template.Library()
#
# @register.simple_tag
# def get_categories():
