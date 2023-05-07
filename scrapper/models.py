from django.db import models

# Create your models here.

class Link(models.Model):



    adress = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.name}"