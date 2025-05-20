from django.contrib import admin
from .models import Event, EventImage

class EventImagesInline(admin.TabularInline):
    model = EventImage


class EventAdmin(admin.ModelAdmin):
    # Sets the admin layout for the models.  This is one model & contains some read only fields & generic fields
    inlines = (EventImagesInline,)
    prepopulated_fields = {"slug": ("name",)}

    #readonly_fields = ('slug',)
admin.site.register(Event, EventAdmin)
