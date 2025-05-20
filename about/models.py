from django.db import models
import os

class About(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about_images/')
    def __str__(self):
        return self.name
   
