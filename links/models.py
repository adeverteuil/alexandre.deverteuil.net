from django.core.urlresolvers import reverse
from django.db import models

from taggit.managers import TaggableManager

# Create your models here.
class Bookmark(models.Model):

    url = models.URLField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("links:bookmark_detail", kwargs={'pk': self.pk})

    class Meta:
        ordering = ("-datetime_added",)
