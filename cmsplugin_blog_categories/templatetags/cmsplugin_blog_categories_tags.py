"""Templatetafs for the ``cmsplugin_blog_categories`` app."""
from django import template
from django.db.models import Count

from cmsplugin_blog_categories.models import Category, EntryCategory


register = template.Library()


@register.assignment_tag
def get_category(entry):
    return EntryCategory.objects.get(entry=entry).category


@register.inclusion_tag(
    'cmsplugin_blog_categories/category_links_snippet.html',
    takes_context=True)
def render_category_links(context, exclude_empty=False):
    """Renders a list of all categories in the database."""
    qs = Category.objects.annotate(num_posts=Count('entrycategory'))
    if exclude_empty:
        qs = qs.exclude(num_posts=0)
    context.update({'categories': qs, })
    return context
