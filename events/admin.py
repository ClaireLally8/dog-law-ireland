from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin  # NEW
from .models import Event, EventImage
from django_summernote.admin import SummernoteModelAdmin

class EventImagesInline(admin.TabularInline):
    model = EventImage

# Important: SortableAdminMixin must come BEFORE SummernoteModelAdmin
class EventAdmin(SortableAdminMixin, SummernoteModelAdmin):
    # tell adminsortable2 which field to use
    sortable = "order"

    inlines = (EventImagesInline,)
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ("description",)

    list_display = ("name", "featured", "order", "uploaded_at")
    list_filter = ("featured",)
    search_fields = ("name", "tagline", "description")

    # IMPORTANT: the first (and preferably only) primary ordering must be the sortable field
    ordering = ("order", "-uploaded_at")  # admin-only ordering

    list_per_page = 100
admin.site.register(Event, EventAdmin)
