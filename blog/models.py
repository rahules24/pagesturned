from django.db import models


class Poem(models.Model):
    poem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="shop/images", default="")
    poem = models.TextField(max_length=10000, default="")
    likes = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=500, default="", blank=True)

    def __str__(self):
        return self.title
