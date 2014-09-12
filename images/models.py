from django.db import models

import os.path


def get_image_path(instance, filename):
    return os.path.join("images", instance.collection.slug, filename)


class Collection(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug


class Image(models.Model):

    title = models.CharField(max_length=128)
    slug = models.SlugField()
    original = models.ImageField(
        upload_to=get_image_path,
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
        #TODO extend with my own file management logic.
        import pprint
        print("Pre-save")
        pprint.pprint(vars(self))
        pprint.pprint(args)
        pprint.pprint(kwargs)
        super().save(*args, **kwargs)
        print("Post-save")
        pprint.pprint(vars(self))
