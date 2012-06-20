import datetime

from django.db import models
from django import forms

from armstrong import hatband

from .models import EmbeddedContent, Publisher, Podcast

class PubAdmin (hatband.ModelAdmin):
  list_display = ('name', 'slug', 'url')
  search_fields = ('name', 'slug')
  
class ECAdmin (hatband.ModelAdmin):
  list_display = ('title', 'ctype', 'publisher', 'file')
  list_filter = ('ctype', 'publisher')
  search_fields = ('title', 'file')
  
  fieldsets = (
    (None, {
        'fields': ('title', 'publisher'),
    }),
    
    ('Content', {
        'fields': ('ctype', 'duration', 'keywords', 'url', 'file', 'code'),
    }),
  )
  
  raw_id_fields = ('publisher',)
  
  formfield_overrides = {
    models.TextField: {'widget': forms.Textarea(attrs={'style': 'width: 400px; height: 200px;'})},
  }
  
  autocomplete_lookup_fields = {'fk': ('publisher',)}
  
  def save_model (self, request, obj, form, change):
    obj.pub_date = datetime.datetime.now()
    super(ECAdmin, self).save_model(request, obj, form, change)
    
class PodcastAdmin (hatband.ModelAdmin):
  list_display = ('title', 'slug', 'category', 'author')
  list_filter = ('category', 'author')
  search_fields = ('title', 'slug', 'category', 'author', 'author_email')
  
  fieldsets = (
    (None, {
        'fields': ('title', 'slug', ('category', 'subtitle'), 'keywords', ('author', 'author_email'), 'image', 'summary'),
    }),
    
    ('Publication Information', {
        'fields': ('pub_date', 'pub_status', 'sites', 'access'),
    })
  )
  
  formfield_overrides = {
    models.TextField: {'widget': forms.Textarea(attrs={'style': 'width: 500px; height: 200px;'})},
  }
  
hatband.site.register(Publisher, PubAdmin)
hatband.site.register(EmbeddedContent, ECAdmin)
hatband.site.register(Podcast, PodcastAdmin)
