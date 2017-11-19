from __future__ import unicode_literals

from django.db import models

class AmazonProductResponses(models.Model):
    name = models.CharField(max_length=512, blank=False)
    response = models.TextField(blank=False)

    def __str__(self):
        return self.title

# Create your models here.
