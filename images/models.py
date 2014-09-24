from django.db import models
from django.core.files.move import file_move_safe
from django.conf import settings


class Image(models.Model):

    original = models.ImageField(
        upload_to="image_uploads",
        height_field="original_height",
        width_field="original_width",
        )
    original_height = models.IntegerField(blank=True)
    original_width = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.original.delete(save=False)
        super().delete(*args, **kwargs)
