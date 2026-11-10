from django import template
from django.urls import translate_url
from django.utils.safestring import mark_safe

from apps.pages.models import Credit, Header, Footer, LegalPage

register = template.Library()


@register.simple_tag
def get_header():
    return Header.objects.first()


@register.simple_tag
def get_footer():
    return Footer.objects.first()


@register.simple_tag
def get_credits():
    """Photo credits grouped by author, in order of first appearance: [(author, [url, ...]), ...]."""
    authors = {}
    for credit in Credit.objects.all():
        authors.setdefault(credit.author, []).append(credit.url)
    return list(authors.items())


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


@register.simple_tag(takes_context=True)
def translated_url(context, language):
    """URL of the current page in another language (keeps the SITE_PREFIX subpath)."""
    request = context['request']
    return translate_url(request.path_info, language)
