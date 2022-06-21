from django.db import models

# Create your models here.


class Info(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=256)
    date = models.CharField(max_length=256)

    def __str__(self):
        return self.full_name
