from django import template

register = template.Library()

@register.filter
def compute_rating(value):
    return float(value) / 5.0 * 75.0