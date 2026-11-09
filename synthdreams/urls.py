"""Synth Dreams URL configuration."""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Spanish (default) has no URL prefix; English lives under /en/
urlpatterns += i18n_patterns(
    path('', include('apps.pages.urls', namespace='pages')),
    prefix_default_language=False,
)

# Admin titles
admin.site.site_header = "Synth Dreams"
admin.site.index_title = "Content admin"
admin.site.site_title = "Synth Dreams"
