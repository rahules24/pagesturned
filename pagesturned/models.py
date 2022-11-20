from django.db import models


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    desc = models.CharField(max_length=1500)

    def __str__(self):
        return self.name
