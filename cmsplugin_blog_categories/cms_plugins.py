"""CMS Plugins for the ``cmsplugin_blog_categories`` app."""
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_blog_categories.models import CategoryPlugin


class CMSCategoryPlugin(CMSPluginBase):
    model = CategoryPlugin
    name = _('Blog Category')
    render_template = 'cmsplugin_blog_categories/category_plugin.html'

    def render(self, context, instance, placeholder):
        entries = instance.category.get_entries()
        context.update({
            'category': instance.category,
            'category_entries': entries,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CMSCategoryPlugin)
