from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource


class ResourceAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ('description',)

admin.site.register(Resource, ResourceAdmin)
