from django.db import models

class Page(models.Model):
    
    title = models.CharField(max_length=64)
    body = models.TextField()
    public = models.BooleanField(default=False)
    description = models.TextField()
