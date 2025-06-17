from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource, ResourceImage

class ResourceImagesInline(admin.TabularInline):
    model = ResourceImage

class ResourceAdmin(SummernoteModelAdmin):
    inlines = (ResourceImagesInline,)
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ('description',)

admin.site.register(Resource, ResourceAdmin)