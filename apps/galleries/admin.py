from django.contrib import admin

# Third-party
from model_clone import CloneModelAdmin
from adminsortable.admin import SortableAdmin

from .models import FirstGalleryImage, SecondGalleryImage


@admin.register(FirstGalleryImage)
class FirstGalleryImageAdmin(SortableAdmin, CloneModelAdmin):
    pass


@admin.register(SecondGalleryImage)
class SecondGalleryImageAdmin(SortableAdmin, CloneModelAdmin):
    pass
