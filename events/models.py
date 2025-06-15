from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import os



class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    tagline = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    event_location = models.CharField(max_length=100, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    URL = models.URLField(blank=True)
    url_name = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.featured:
            Event.objects.exclude(pk=self.pk).update(featured=False)
        self.full_clean()  # call clean() method before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')

class EventLink(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='links')
    url = models.URLField()
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.url})"