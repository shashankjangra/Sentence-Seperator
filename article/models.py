from django.db import models

# Create your models here.
class Output(models.Model):
    sentence = models.TextField()
    highlight = models.BooleanField(default=False)