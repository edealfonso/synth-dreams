from django.db import models

# Third-party
from adminsortable.models import SortableMixin
from model_clone import CloneMixin

from apps.pages.models import image_preview


class GalleryImage(CloneMixin, SortableMixin):
    """Sortable image for one of the home galleries."""

    image = models.ImageField(blank=True)

    # special fields
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return image_preview(self.image)

    class Meta:
        abstract = True
        ordering = ['the_order']


class FirstGalleryImage(GalleryImage):

    class Meta(GalleryImage.Meta):
        verbose_name = "Image"
        verbose_name_plural = "Gallery 1 images"


class SecondGalleryImage(GalleryImage):

    class Meta(GalleryImage.Meta):
        verbose_name = "Image"
        verbose_name_plural = "Gallery 2 images"
