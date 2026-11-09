from django import template

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
