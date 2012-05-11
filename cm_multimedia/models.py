from django.db import models
from django.conf import settings

from armstrong.apps.content.models import Content

UPLOAD_PATH = getattr(settings, 'CM_IMAGE_UPLOAD_PATH', 'cm/mutlimedia/')
CONTENT_TYPES = (
  ('audio', 'Audio'),
  ('other', 'Other'),
  ('video', 'Video'),
)

class EmbeddedContent (Content):
  url = models.URLField('URL', blank=True, null=True, help_text='Fill in one URL, File, or Embed Code')
  file = models.FileField(upload_to=UPLOAD_PATH, blank=True, null=True)
  code = models.TextField('Embed Code', blank=True, null=True)
  
  ctype = models.CharField('Content Type', choices=CONTENT_TYPES, max_length=25)
  
  class Meta:
    verbose_name_plural = 'Embedded Content'
    