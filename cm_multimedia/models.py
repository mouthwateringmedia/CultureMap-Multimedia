from django.db import models
from django.conf import settings

from armstrong.apps.content.models import Content

UPLOAD_PATH = getattr(settings, 'CM_IMAGE_UPLOAD_PATH', 'cm/mutlimedia/')
CONTENT_TYPES = (
  ('audio', 'Audio'),
  ('doc', 'Document'),
  ('other', 'Other'),
  ('video', 'Video'),
)

class Publisher (models.Model):
  name = models.CharField(max_length=175)
  url = models.URLField('URL', blank=True, null=True)
  slug = models.SlugField()
  
  def __unicode__ (self):
    return self.name
    
  @staticmethod
  def autocomplete_search_fields ():
    return ("id__iexact", "name__icontains", "slug__icontains")
    
  class Meta:
    ordering = ('name',)
    
class EmbeddedContent (Content):
  url = models.URLField('URL', blank=True, null=True, help_text='Fill in one URL, File, or Embed Code')
  file = models.FileField(upload_to=UPLOAD_PATH, blank=True, null=True)
  code = models.TextField('Embed Code', blank=True, null=True)
  
  ctype = models.CharField('Content Type', choices=CONTENT_TYPES, max_length=25)
  
  publisher = models.ForeignKey(Publisher, blank=True, null=True)
  
  class Meta:
    verbose_name_plural = 'Embedded Content'
    