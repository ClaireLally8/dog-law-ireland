from django.db import models

class resource(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    pdf = models.FileField()
    link = models.URLField()
    
    
