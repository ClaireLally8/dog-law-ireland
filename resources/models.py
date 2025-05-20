from django.db import models
from django.core.exceptions import ValidationError

class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='resource_files/', blank=True, null=True)
    image = models.ImageField(upload_to='resources_images/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Require at least one upload (optional, remove if not needed)
        if not self.file and not self.image:
            raise ValidationError('Please upload at least an image or a file.')

        # Validate file is PDF if a file is uploaded
        if self.file:
            if not self.file.name.lower().endswith('.pdf'):
                raise ValidationError('Uploaded file must be a PDF.')

    def __str__(self):
        return self.name
