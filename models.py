from django.db import models
import django.contrib.admin.models


class Category(models.Model):

    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=256)
    slug = models.SlugField()
    pub_date = models.DateTimeField("date published")
    body = models.TextField()
    summary = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, null=True, blank=True)

    def mod_date(self):
        """Retrieve last modification date from the admin module's log."""
        try:
            return django.contrib.admin.models.LogEntry.objects.filter(
                content_type__app_label__exact="blog",
                content_type__model__exact="post",
                action_flag__exact=django.contrib.admin.models.CHANGE,
                object_id__exact=self.pk,
                ).order_by(
                    "-action_time"
                    )[0].action_time
        except IndexError:
            return self.pub_date

    def __str__(self):
        return self.title
