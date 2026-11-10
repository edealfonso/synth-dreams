from django.contrib import admin

# Third-party
from adminsortable.admin import SortableAdmin
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TranslationAdmin
from model_clone import CloneModelAdmin

from .models import Header, Footer, Home, Vignette, MagnifyItem, LegalPage, image_preview


@admin.register(Header)
class HeaderAdmin(SingletonModelAdmin, TranslationAdmin):
    pass


@admin.register(Footer)
class FooterAdmin(SingletonModelAdmin, TranslationAdmin):
    pass


@admin.register(Home)
class HomeAdmin(SingletonModelAdmin, TranslationAdmin):

    # one collapsible fieldset per block, in page order
    fieldsets = (
        ('s01 · Pinned cover', {
            'classes': ('collapse',),
            'fields': (
                's01_logo',
                ('s01_image', 's01_image_mobile'),
            ),
        }),
        ('s02 · Parallax with title', {
            'classes': ('collapse',),
            'fields': (
                's02_title',
                's02_image',
                's02_text',
            ),
        }),
        ('s03 · Statement', {
            'classes': ('collapse',),
            'fields': (
                's03_text',
            ),
        }),
        ('s04 · Video cover', {
            'classes': ('collapse',),
            'fields': (
                ('s04_video_high', 's04_video_low', 's04_video_poster'),
            ),
        }),
        ('s05 · Parallax', {
            'classes': ('collapse',),
            'fields': (
                's05_text',
                's05_image',
            ),
        }),
        ('s06 · Three horizontal steps', {
            'classes': ('collapse',),
            'fields': (
                ('s06_step_title1', 's06_step_text1'),
                ('s06_step_title2', 's06_step_text2'),
                ('s06_step_title3', 's06_step_text3'),
            ),
        }),
        ('s07 · Pinned gallery', {
            'classes': ('collapse',),
            'fields': (
                's07_title',
                's07_text',
            ),
        }),
        ('s08 · Parallax layout', {
            'classes': ('collapse',),
            'fields': (
                's08_title',
                ('s08_image1', 's08_image1_mobile'),
                's08_text',
                ('s08_image2', 's08_image2_mobile'),
            ),
        }),
        ('s09 · Floating vignettes', {
            'classes': ('collapse',),
            'fields': (
                's09_title',
                's09_text',
                's09_left_image',
                ('s09_group_title1', 's09_group_title2', 's09_group_title3'),
                's09_group_image3',
            ),
        }),
        ('s10 · Image or video', {
            'classes': ('collapse',),
            'fields': (
                's10_title',
                's10_text',
                's10_image',
                ('s10_video_high', 's10_video_low', 's10_video_poster'),
            ),
        }),
        ('s11 · Rising text over pinned image', {
            'classes': ('collapse',),
            'fields': (
                's11_title',
                's11_text',
                's11_image',
            ),
        }),
        ('s12 · Pinned gallery', {
            'classes': ('collapse',),
            'fields': (
                's12_title',
                's12_text',
            ),
        }),
        ('s13 · Pinned cover', {
            'classes': ('collapse',),
            'fields': (
                's13_title',
                's13_text',
                's13_image',
            ),
        }),
        ('s14 · Magnify list', {
            'classes': ('collapse',),
            'fields': (
                's14_image',
                's14_text',
            ),
        }),
        ('s15 · Split images', {
            'classes': ('collapse',),
            'fields': (
                's15_title_line1',
                's15_title_line2',
                's15_image_left',
                's15_image_right',
                's15_text',
            ),
        }),
        ('s16 · Vertical points', {
            'classes': ('collapse',),
            'fields': (
                's16_title',
                's16_text',
                's16_image',
                ('s16_point_title1', 's16_point_text1'),
                ('s16_point_title2', 's16_point_text2'),
                ('s16_point_title3', 's16_point_text3'),
            ),
        }),
        ('s17 · Full image with text', {
            'classes': ('collapse',),
            'fields': (
                's17_text',
                's17_image',
            ),
        }),
    )


@admin.register(Vignette)
class VignetteAdmin(SortableAdmin, CloneModelAdmin, TranslationAdmin):

    @admin.display(description='Image')
    def preview(self, obj):
        return image_preview(obj.image)

    list_display = ['preview', 'group', 'kind']


@admin.register(MagnifyItem)
class MagnifyItemAdmin(SortableAdmin, CloneModelAdmin, TranslationAdmin):
    pass


@admin.register(LegalPage)
class LegalPageAdmin(SortableAdmin, CloneModelAdmin, TranslationAdmin):
    pass
