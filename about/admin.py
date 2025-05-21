from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # If you want to be able to edit file in the form, just ensure it's not excluded
    # Don't exclude or make readonly your file/image field!

    def save_model(self, request, obj, form, change):
        if request.FILES:
            print("FILES RECEIVED IN ADMIN:", request.FILES)
        else:
            print("NO FILES RECEIVED IN ADMIN")
        super().save_model(request, obj, form, change)
