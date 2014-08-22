from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField("date published")
    body = models.TextField()
    summary = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, null=True, blank=True)

    def __str__(self):
        return self.title
