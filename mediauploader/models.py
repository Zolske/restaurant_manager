from django.db import models

class media(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icons/', blank=True)