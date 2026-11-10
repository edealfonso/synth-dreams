from modeltranslation.translator import translator, TranslationOptions

from .models import Header, Home, Vignette, MagnifyItem, Footer, LegalPage

# Each translatable field gets an _es and an _en column (see LANGUAGES in settings).


class HeaderTranslationOptions(TranslationOptions):
    fields = ('contact_link_text',)


translator.register(Header, HeaderTranslationOptions)


class HomeTranslationOptions(TranslationOptions):
    fields = (
        # s02 · parallax with title
        's02_title', 's02_text',
        # s03 · statement
        's03_text',
        # s05 · parallax
        's05_text',
        # s06 · three horizontal steps
        's06_step_title1', 's06_step_text1', 's06_step_title2', 's06_step_text2', 's06_step_title3', 's06_step_text3',
        # s07 · pinned gallery
        's07_title', 's07_text',
        # s08 · parallax layout
        's08_title', 's08_text',
        # s09 · floating vignettes
        's09_title', 's09_text', 's09_group_title1', 's09_group_title2', 's09_group_title3',
        # s10 · image or video
        's10_title', 's10_text',
        # s11 · rising text over pinned image
        's11_title', 's11_text',
        # s12 · pinned gallery
        's12_title', 's12_text',
        # s13 · pinned cover
        's13_title', 's13_text',
        # s14 · magnify list
        's14_text',
        # s15 · split images
        's15_title_line1', 's15_title_line2', 's15_text',
        # s16 · vertical points
        's16_title', 's16_text', 's16_point_title1', 's16_point_text1', 's16_point_title2', 's16_point_text2', 's16_point_title3', 's16_point_text3',
        # s17 · full image with text
        's17_text',
    )


translator.register(Home, HomeTranslationOptions)


class VignetteTranslationOptions(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4')


translator.register(Vignette, VignetteTranslationOptions)


class MagnifyItemTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


translator.register(MagnifyItem, MagnifyItemTranslationOptions)


class FooterTranslationOptions(TranslationOptions):
    fields = ('text', 'map_link_text', 'contact_details', 'credits_label', 'credits_text')


translator.register(Footer, FooterTranslationOptions)


class LegalPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(LegalPage, LegalPageTranslationOptions)
