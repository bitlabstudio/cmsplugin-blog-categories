"""Tests for models of the ``cmsplugin_blog_categories``` application."""
from django.test import TestCase

from cmsplugin_blog_categories.tests.factories import (
    CategoryFactory,
    CategoryTitleENFactory,
    EntryCategoryFactory,
    EntryFactory,
)


class CategoryTestCase(TestCase):
    """Tests for the ``Category`` model class."""
    longMessage = True

    def setUp(self):
        self.obj = CategoryFactory()

    def test_model(self):
        self.assertTrue(self.obj.pk)

    def test_translation(self):
        self.assertFalse(self.obj.get_translation())
        CategoryTitleENFactory(enquiry=self.obj)
        self.assertEqual(self.obj.get_translation().title, 'A question?')


class EntryTestCase(TestCase):
    """Tests for the ``Entry`` model class."""
    longMessage = True

    def setUp(self):
        self.obj = EntryFactory()

    def test_model(self):
        self.assertTrue(self.obj.pk)


class EntryCategoryTestCase(TestCase):
    """Tests for the ``EntryCategory`` model class."""
    longMessage = True

    def setUp(self):
        self.obj = EntryCategoryFactory()

    def test_model(self):
        self.assertTrue(self.obj.pk)
