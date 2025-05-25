from django.db import models
from django.core.exceptions import ValidationError

class Resource(models.Model):
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)
    video = models.URLField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Require at least one upload (optional, remove if not needed)
        if not self.file and not self.image:
            raise ValidationError('Please upload at least an image or a file.')
        # Validate file is PDF if a file is uploaded
        if self.file:
            if not self.file.name.lower().endswith('.pdf'):
                raise ValidationError('Uploaded file must be a PDF.')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name or "resource")
            slug = base_slug
            counter = 1
            while Resource.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)   
    def __str__(self):
        return self.name
