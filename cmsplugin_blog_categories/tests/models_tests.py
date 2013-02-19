"""Tests for models of the ``cmsplugin_blog_categories``` application."""
from django.test import TestCase

from cmsplugin_blog_categories.tests.factories import (
    CategoryFactory,
    CategoryTitleCNFactory,
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

    def test_get_title(self):
        self.assertEqual(self.obj.get_title(), 'None')
        CategoryTitleENFactory(category=self.obj)
        self.assertEqual(self.obj.get_title(), 'Category Title')


class CategoryTitleTestCase(TestCase):
    """Tests for the ``CategoryTitle`` model class."""
    longMessage = True

    def setUp(self):
        self.obj_en = CategoryTitleENFactory()
        self.obj_cn = CategoryTitleCNFactory()

    def test_model(self):
        self.assertTrue(self.obj_en.pk)
        self.assertTrue(self.obj_cn.pk)


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
