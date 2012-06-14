import mimetypes

from django import template

register = template.Library()

mimetypes.init()

@register.filter
def get_mime (filename):
  m, encoding = mimetypes.guess_type(filename)
  if m is None:
    m = 'application/octet-stream'
    
  return m
  