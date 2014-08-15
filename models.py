from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField("date_published")
    body = models.TextField()
    public = models.BooleanField(default=False)
