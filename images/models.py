from django.db import models
from django.core.files.move import file_move_safe
from django.conf import settings

import os.path


# Removing this obsolete name breaks migration number 0001.
def get_image_path(): pass


class Collection(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Subdirectory of MEDIA_URL to hold collections under.
    dir = os.path.join(settings.MEDIA_URL, "images")

    def __init__(self, *args, **kwargs):
        # Save slug for later comparison in save method.
        super().__init__(*args, **kwargs)
        self.initial_slug = self.slug

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class Image(models.Model):

    title = models.CharField(max_length=128)
    basename = models.CharField(max_length=128)
    original_basename = models.CharField(
        max_length=128,
        blank=True,
        editable=False,
        )
    original = models.ImageField(
        upload_to=os.path.join(Collection.subdir, "uploads"),
        height_field="original_height",
        width_field="original_width",
        )
    original_height = models.IntegerField(blank=True)
    original_width = models.IntegerField(blank=True)
    collection = models.ForeignKey(Collection)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def _get_file_name(self):
        basename = os.path.basename(self.original.name)
        if self.slug:
            basename = self.slug
        return os.path.join(
            self.original.storage.base_location,
            "images",
            self.collection.slug,
            basename,
            )

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
