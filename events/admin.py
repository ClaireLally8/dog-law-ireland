from django.contrib import admin
from .models import Event, EventImage
from django_summernote.admin import SummernoteModelAdmin

class EventImagesInline(admin.TabularInline):
    model = EventImage

class EventAdmin(SummernoteModelAdmin):  # Inherit from SummernoteModelAdmin
    inlines = (EventImagesInline,)
    prepopulated_fields = {"slug": ("name",)}
    
    # Specify which fields to decorate
    summernote_fields = ('description',)  # Replace 'description' with the name of your text field

admin.site.register(Event, EventAdmin)
