"""Tests for tags of the ``cmsplugin_blog_categories``` application."""
from django.test import TestCase

from cmsplugin_blog_categories.templatetags import (
    cmsplugin_blog_categories_tags as tags,
)
from cmsplugin_blog_categories.tests.factories import (
    CategoryFactory,
    EntryFactory,
    EntryCategoryFactory,
)


class GetCategoryTestCase(TestCase):
    """Tests for the ``get_category`` tag."""
    longMessage = True

    def setUp(self):
        self.entry = EntryFactory()
        self.category = EntryCategoryFactory()

    def test_tag(self):
        self.assertFalse(tags.get_category())
        self.assertFalse(tags.get_category(self.entry))
        self.assertEqual(tags.get_category(self.category.entry),
                         [self.category.category])


class RenderCategoryLinksTestCase(TestCase):
    """Tests for the ``render_category_links`` tag."""
    longMessage = True

    def setUp(self):
        self.entry_category = EntryCategoryFactory()
        self.category = CategoryFactory()

    def test_tag(self):
        self.assertEqual(tags.render_category_links({}).get('categories')[0],
                         self.entry_category.category)
        self.assertEqual(
            tags.render_category_links({}, True).get('categories').count(), 1)
