from django import template

from product.models import Category

register = template.Library()


@register.simple_tag
def categorylist():
    return Category.objects.all()