from django.db import models
from django.utils.html import format_html

# Third-party
from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from adminsortable.models import SortableMixin
from autoslug import AutoSlugField
from model_clone import CloneMixin

from .choices import VIGNETTE_GROUPS, VIGNETTE_KINDS


def image_preview(field):
    """Small <img> for admin lists (empty string if there is no file)."""
    if not field:
        return '(no image)'
    return format_html('<img src="{0}" class="admin-previews" />', field.url)


# HEADER

class Header(SingletonModel):

    logo = models.FileField(blank=True, null=True)
    contact_link_text = models.CharField(default="Contact", max_length=255, blank=True, null=True)
    language_selector_es = models.CharField(max_length=255, blank=True, null=True)
    language_selector_en = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Header"

    class Meta:
        verbose_name = "Header"


# HOME

class Home(SingletonModel):
    """One-page home. Fields are prefixed with the block they belong to (sNN_, in page order)."""

    # s01 · pinned cover
    s01_logo = models.FileField(blank=True, null=True)
    s01_image = models.ImageField(blank=True)
    s01_image_mobile = models.ImageField(blank=True)

    # s02 · parallax with title
    s02_title = models.CharField(max_length=255, blank=True, null=True)
    s02_image = models.FileField(blank=True)
    s02_text = RichTextField(null=True, blank=True)

    # s03 · statement
    s03_text = RichTextField(null=True, blank=True)

    # s04 · video cover
    s04_video_high = models.FileField(upload_to='video', blank=True, null=True)
    s04_video_low = models.FileField(upload_to='video', blank=True, null=True)
    s04_video_poster = models.FileField(upload_to='video', blank=True, null=True)

    # s05 · parallax
    s05_text = RichTextField(null=True, blank=True)
    s05_image = models.ImageField(blank=True)

    # s06 · three horizontal steps
    s06_step_title1 = models.CharField(max_length=255, blank=True, null=True)
    s06_step_text1 = RichTextField(null=True, blank=True)
    s06_step_title2 = models.CharField(max_length=255, blank=True, null=True)
    s06_step_text2 = RichTextField(null=True, blank=True)
    s06_step_title3 = models.CharField(max_length=255, blank=True, null=True)
    s06_step_text3 = RichTextField(null=True, blank=True)

    # s07 · pinned gallery (images: galleries.FirstGalleryImage)
    s07_title = models.CharField(max_length=255, blank=True, null=True)
    s07_text = RichTextField(null=True, blank=True)

    # s08 · parallax layout
    s08_title = models.CharField(max_length=255, blank=True, null=True)
    s08_image1 = models.ImageField(blank=True)
    s08_image1_mobile = models.ImageField(blank=True)
    s08_text = RichTextField(null=True, blank=True)
    s08_image2 = models.ImageField(blank=True)
    s08_image2_mobile = models.ImageField(blank=True)

    # s09 · floating vignettes (vignettes: Vignette, one title per group)
    s09_title = models.CharField(max_length=255, blank=True, null=True)
    s09_text = RichTextField(null=True, blank=True)
    s09_left_image = models.FileField(blank=True)
    s09_group_title1 = models.TextField(max_length=255, blank=True)
    s09_group_title2 = models.TextField(max_length=255, blank=True)
    s09_group_title3 = models.TextField(max_length=255, blank=True)

    # s10 · image or video
    s10_title = models.CharField(max_length=255, blank=True, null=True)
    s10_text = RichTextField(null=True, blank=True)
    s10_image = models.ImageField(blank=True)
    s10_video_high = models.FileField(upload_to='video', blank=True, null=True)
    s10_video_low = models.FileField(upload_to='video', blank=True, null=True)
    s10_video_poster = models.FileField(upload_to='video', blank=True, null=True)

    # s11 · rising text over pinned image
    s11_title = models.CharField(max_length=255, blank=True, null=True)
    s11_text = RichTextField(null=True, blank=True)
    s11_image = models.ImageField(blank=True)

    # s12 · pinned gallery (images: galleries.SecondGalleryImage)
    s12_title = models.CharField(max_length=255, blank=True, null=True)
    s12_text = RichTextField(null=True, blank=True)

    # s13 · pinned cover
    s13_title = models.CharField(max_length=255, blank=True, null=True)
    s13_text = RichTextField(null=True, blank=True)
    s13_image = models.ImageField(blank=True)

    # s14 · magnify list (items: MagnifyItem)
    s14_image = models.ImageField(blank=True)
    s14_text = RichTextField(null=True, blank=True)

    # s15 · split images
    s15_title_line1 = models.CharField(max_length=255, blank=True, null=True)
    s15_title_line2 = models.CharField(max_length=255, blank=True, null=True)
    s15_image_left = models.ImageField(blank=True)
    s15_image_right = models.ImageField(blank=True)
    s15_text = RichTextField(null=True, blank=True)

    # s16 · vertical points
    s16_title = models.CharField(max_length=255, blank=True, null=True)
    s16_text = RichTextField(null=True, blank=True)
    s16_image = models.ImageField(blank=True)
    s16_point_title1 = models.CharField(max_length=255, blank=True, null=True)
    s16_point_text1 = RichTextField(null=True, blank=True)
    s16_point_title2 = models.CharField(max_length=255, blank=True, null=True)
    s16_point_text2 = RichTextField(null=True, blank=True)
    s16_point_title3 = models.CharField(max_length=255, blank=True, null=True)
    s16_point_text3 = RichTextField(null=True, blank=True)

    # s17 · full image with text
    s17_text = RichTextField(null=True, blank=True)
    s17_image = models.ImageField(blank=True)

    def __str__(self):
        return "Home"

    class Meta:
        verbose_name = "Home"


class Vignette(CloneMixin, SortableMixin):
    """s09 · one vignette of the floating vignettes block."""

    group = models.CharField(max_length=1, choices=VIGNETTE_GROUPS, blank=True, null=True)
    kind = models.CharField(max_length=10, choices=VIGNETTE_KINDS, blank=True, null=True)

    image = models.FileField(blank=True, null=True)
    text1 = RichTextField(null=True, blank=True)
    text2 = RichTextField(null=True, blank=True)
    text3 = RichTextField(null=True, blank=True)

    extra_image = models.FileField(blank=True, null=True)

    # special fields
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return image_preview(self.image)

    class Meta:
        ordering = ['the_order']
        verbose_name = "Vignette"
        verbose_name_plural = "Home – s09 · Vignettes"


class MagnifyItem(CloneMixin, SortableMixin):
    """s14 · one entry of the magnify list."""

    title = models.CharField(max_length=255, blank=True, null=True)
    text = RichTextField(null=True, blank=True)

    # special fields
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        ordering = ['the_order']
        verbose_name = "Magnify item"
        verbose_name_plural = "Home – s14 · Magnify items"


# FOOTER

class Footer(SingletonModel):

    text = RichTextField(null=True, blank=True)
    map_link_text = models.CharField(max_length=255, blank=True, null=True)
    map = models.FileField(blank=True, null=True)
    contact_details = RichTextField(null=True, blank=True)

    social_title = models.CharField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=1000, null=True, blank=True)
    linkedin = models.URLField(max_length=1000, null=True, blank=True)
    pinterest = models.URLField(max_length=1000, null=True, blank=True)
    wikipedia = models.URLField(max_length=1000, null=True, blank=True)

    bottom_image = models.ImageField(blank=True)
    copyright = models.CharField(default="© Elsa de Alfonso", max_length=255, blank=True, null=True)

    def __str__(self):
        return "Footer"

    class Meta:
        verbose_name = "Footer"


class LegalPage(SortableMixin):

    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(null=True, blank=True)

    # special fields
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    slug = AutoSlugField(populate_from='title', editable=False, unique=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        ordering = ['the_order']
        verbose_name = "Legal page"
        verbose_name_plural = "Legal pages"
