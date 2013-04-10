"""Tests for models of the ``cmsplugin_blog_categories``` application."""
from django.test import TestCase

from ..cms_plugins import CMSCategoryPlugin
from .factories import CategoryTitleENFactory, CategoryPluginFactory


class CMSCategoryPluginTestCase(TestCase):
    """Tests for the ``CMSCategoryPlugin`` cmsplugin."""
    longMessage = True

    def setUp(self):
        self.plugin = CategoryPluginFactory()
        self.title = CategoryTitleENFactory()
        self.plugin.categories.add(self.title.category)
        self.cmsplugin = CMSCategoryPlugin()

    def test_render(self):
        context = self.cmsplugin.render(context={}, instance=self.plugin,
                                        placeholder=None)
        self.assertEqual(context['entries'], [])
