from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource, ResourceImage


class ResourceImagesInline(admin.TabularInline):
    model = ResourceImage
    extra = 0


@admin.register(Resource)
class ResourceAdmin(SortableAdminMixin, SummernoteModelAdmin):
    # use the renamed field
    sortable = "position"

    inlines = (ResourceImagesInline,)
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ("description",)

    # keep the changelist primarily ordered by the sortable field
    ordering = ("position", "-uploaded_at")

    # nice-to-haves
    list_display = ("name", "position", "uploaded_at")
    search_fields = ("name", "tagline", "description")
    list_per_page = 100
