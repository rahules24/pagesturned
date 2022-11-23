from django.db import models
from django.utils.timezone import now


class Poem(models.Model):
    poem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    genre = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="blog/images", default="")
    poem = models.TextField(max_length=10000, default="")
    date_added = models.DateField(default=now)
    likes = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=500, default="", blank=True)

    def __str__(self):
        return self.title
