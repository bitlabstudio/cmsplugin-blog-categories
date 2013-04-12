"""CMS Plugins for the ``cmsplugin_blog_categories`` app."""
from django.utils.timezone import now
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CategoryPlugin, EntryCategory


class CMSCategoryPlugin(CMSPluginBase):
    model = CategoryPlugin
    name = _('Blog Category')
    render_template = 'cmsplugin_blog_categories/category_plugin.html'

    def render(self, context, instance, placeholder):
        qs = EntryCategory.objects.select_related().filter(
            category__in=instance.categories.all(), entry__is_published=True,
            entry__pub_date__lte=now()).order_by('-entry__pub_date')
        context.update({
            'entries': [item.entry for item in qs],
            'placeholder': placeholder,
        })
        if instance.template_argument:
            context.update({'{0}'.format(instance.template_argument): True, })
        return context

plugin_pool.register_plugin(CMSCategoryPlugin)
