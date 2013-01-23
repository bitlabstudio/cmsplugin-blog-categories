"""Templatetafs for the ``cmsplugin_blog_categories`` app."""
from django import template

from cmsplugin_blog_categories.models import Category, EntryCategory


register = template.Library()


@register.assignment_tag
def get_category(entry):
    return EntryCategory.objects.get(entry=entry).category


@register.inclusion_tag(
    'cmsplugin_blog_categories/category_links_snippet.html',
    takes_context=True)
def render_category_links(context):
    """Renders a list of all categories in the database."""
    context.update({
        'categories': Category.objects.all()
    })
    return context
