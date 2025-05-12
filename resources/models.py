from django.db import models
from django.core.exceptions import ValidationError
import os

class Resource(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    file = models.FileField(upload_to='resources/files/', blank=True, null=True)
    image = models.ImageField(upload_to='resources/images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.file:
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext != '.pdf':
                raise ValidationError('Only PDF files are allowed.')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.full_clean()  # call clean() method before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
