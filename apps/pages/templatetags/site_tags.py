from django import template
from django.utils.safestring import mark_safe

from apps.pages.models import Header, Footer, LegalPage

register = template.Library()


@register.simple_tag
def get_header():
    return Header.objects.first()


@register.simple_tag
def get_footer():
    return Footer.objects.first()


@register.simple_tag
def get_legal_pages():
    return LegalPage.objects.all()


@register.filter
def media_url(field):
    """URL of a FileField/ImageField, or '' if it is empty (field.url raises ValueError when there is no file)."""
    try:
        return field.url if field else ''
    except ValueError:
        return ''


@register.filter
def inline_svg(field):
    """Contents of an uploaded SVG file, to render it inline (so the JS can animate its parts), or ''.

    Only for files uploaded from the admin, which are trusted.
    """
    if not field or not field.name.lower().endswith('.svg'):
        return ''
    try:
        with field.open('rb') as f:
            return mark_safe(f.read().decode('utf-8'))
    except (OSError, ValueError):
        return ''
