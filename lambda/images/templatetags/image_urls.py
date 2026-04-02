"""
Template tags for building image URLs via CloudFront / IMAGE_BASE_URL.
Replaces the old easy-thumbnails {% thumbnail %} tag and {{ image.file.url }}.
"""

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def image_url(image):
    """Return the full-size image URL.

    Usage:  {% image_url image %}
    """
    base = settings.IMAGE_BASE_URL.rstrip("/")
    return f"{base}/{image.file}"


@register.simple_tag
def thumbnail_url(image):
    """Return the pre-generated 350x350 thumbnail URL.

    The old easy-thumbnails naming convention was:
        <filename>.350x350_q85_crop_upscale.jpg

    Usage:  {% thumbnail_url image %}
    """
    base = settings.IMAGE_BASE_URL.rstrip("/")
    return f"{base}/{image.file}.350x350_q85_crop_upscale.jpg"
