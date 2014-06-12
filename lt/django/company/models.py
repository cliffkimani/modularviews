from django.db import models
from django.conf import settings

from cms.models import CMSPlugin

logo_upload = getattr(settings,'COMPANY_LOGO_UPLOAD_TO','companies/')

class CompanyPlugin(CMSPlugin):
    name = models.CharField(max_length=255, blank=False)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    """
    logo_height = models.PositiveSmallIntegerField(editable=False,
                                                   null=True,
                                                   blank=True)
  
    logo_width = models.PositiveSmallIntegerField(editable=False,
                                                  null=True,
                                                  blank=True)
    """
    logo = models.ImageField(upload_to=logo_upload,
                             #height_field='logo_height',
                             #width_field='logo_width',
                             blank=True)