from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource, ResourceImage, ResourceLink

class ResourceImageInline(admin.TabularInline):
    model = ResourceImage
    extra = 1
    fields = ('image', 'is_banner', 'is_thumbnail')

class ResourceLinkInline(admin.TabularInline):
    model = ResourceLink
    extra = 1
    fields = ('name', 'url')

@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'uploaded_at')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)
    inlines = [ResourceImageInline, ResourceLinkInline]

