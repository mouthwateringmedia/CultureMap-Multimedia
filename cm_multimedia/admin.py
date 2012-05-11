import datetime

from django.db import models
from django import forms

from armstrong import hatband

from .models import EmbeddedContent

class ECAdmin (hatband.ModelAdmin):
  list_display = ('title', 'slug', 'ctype')
  list_filter = ('ctype',)
  search_fields = ('title', 'slug')
  
  fieldsets = (
    (None, {
        'fields': ('title', 'slug'),
    }),
    
    ('Content', {
        'fields': ('ctype', 'url', 'file', 'code'),
    }),
  )
  
  formfield_overrides = {
    models.TextField: {'widget': forms.Textarea(attrs={'style': 'width: 400px; height: 200px;'})},
  }
  
  def save_model (self, request, obj, form, change):
    obj.pub_date = datetime.datetime.now()
    super(ECAdmin, self).save_model(request, obj, form, change)
    
hatband.site.register(EmbeddedContent, ECAdmin)
