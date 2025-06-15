from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Resource(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    file_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)
    URL = models.URLField(blank=True)
    url_name = models.CharField(max_length=50, blank=True)
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

class ResourceLink(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='links', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.url})"

class ResourceImage(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    is_banner = models.BooleanField(default=False, null=True, blank=True)
    is_thumbnail = models.BooleanField(default=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Ensure only one banner per resource
        if self.is_banner:
            ResourceImage.objects.filter(resource=self.resource, is_banner=True).exclude(pk=self.pk).update(is_banner=False)
        else:
            # If no other image is marked banner, set this one
            if not self.resource.images.exclude(pk=self.pk).filter(is_banner=True).exists():
                self.is_banner = True
                self.save(update_fields=['is_banner'])

        # Ensure only one thumbnail per resource
        if self.is_thumbnail:
            ResourceImage.objects.filter(resource=self.resource, is_thumbnail=True).exclude(pk=self.pk).update(is_thumbnail=False)
        else:
            # If no other image is marked thumbnail, set this one
            if not self.resource.images.exclude(pk=self.pk).filter(is_thumbnail=True).exists():
                self.is_thumbnail = True
                self.save(update_fields=['is_thumbnail'])

    def __str__(self):
        return f"Image for {self.resource.name}"
