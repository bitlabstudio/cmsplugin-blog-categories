"""Tests for models of the ``cmsplugin_blog_categories``` application."""
from django.test import TestCase

from cmsplugin_blog_categories.cms_plugins import CMSCategoryPlugin
from cmsplugin_blog_categories.tests.factories import CategoryPluginFactory


class CMSCategoryPluginTestCase(TestCase):
    """Tests for the ``CMSCategoryPlugin`` cmsplugin."""
    longMessage = True

    def setUp(self):
        self.plugin = CategoryPluginFactory()
        self.cmsplugin = CMSCategoryPlugin()

    def test_render(self):
        self.assertEqual(
            self.cmsplugin.render(context={}, instance=self.plugin,
                                  placeholder=None),
            {'category': self.plugin.category, 'category_entries': [],
             'placeholder': None})
