from django.db import models
from django.contrib.flatpages.models import FlatPage

class Page(FlatPage):
    
    description = models.CharField(max_length=256)
    pub_date = models.DateTimeField(blank=True, null=True)
