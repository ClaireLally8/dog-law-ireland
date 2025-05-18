from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import os

class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    #file = models.FileField(upload_to='events/files/', blank=True, null=True)
    #image = models.ImageField(upload_to='events/images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.full_clean()  # call clean() method before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')
