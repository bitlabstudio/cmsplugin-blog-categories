"""Templatetafs for the ``cmsplugin_blog_categories`` app."""
from django import template

from cmsplugin_blog_categories.models import Category


register = template.Library()


@register.inclusion_tag(
    'cmsplugin_blog_categories/category_links_snippet.html',
    takes_context=True)
def render_category_links(context):
    context.update({
        'categories': Category.objects.all()
    })
    return context
