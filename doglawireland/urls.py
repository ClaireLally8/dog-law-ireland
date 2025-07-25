from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about/', include('about.urls')),
    path('events/', include('events.urls')),
    path('resources/', include('resources.urls')),
    path('summernote/', include('django_summernote.urls')),
]