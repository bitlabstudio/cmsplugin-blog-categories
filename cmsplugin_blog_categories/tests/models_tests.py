"""Tests for models of the ``cmsplugin_blog_categories``` application."""
from django.test import TestCase

from cmsplugin_blog_categories.tests.factories import (
    CategoryTitleCNFactory,
    CategoryTitleENFactory,
    EntryCategoryFactory,
)


class CategoryTestCase(TestCase):
    """Tests for the ``Category`` model class."""
    longMessage = True

    def setUp(self):
        self.category_title = CategoryTitleENFactory()
        self.category = self.category_title.category

    def test_model(self):
        """Should be able to instantiate and save the model."""
        self.assertTrue(self.category.pk)

    def test_get_entries(self):
        """Should return all entries that have this category."""
        ec = EntryCategoryFactory()
        result = ec.category.get_entries()
        self.assertEqual(result, [ec.entry, ])

    def test_get_title(self):
        """
        Should return the title in the best available translation.

        Note: We assume that there will always be at least one translation
        for the objet, since it is impossible to save a Category in the admin
        without also creating the first CategoryTitle for that object.

        """
        result = self.category.get_title()
        self.assertEqual(result, 'Category Title')


class CategoryTitleTestCase(TestCase):
    """Tests for the ``CategoryTitle`` model class."""
    longMessage = True

    def setUp(self):
        self.obj_en = CategoryTitleENFactory()
        self.obj_cn = CategoryTitleCNFactory()

    def test_model(self):
        self.assertTrue(self.obj_en.pk)
        self.assertTrue(self.obj_cn.pk)


class EntryCategoryTestCase(TestCase):
    """Tests for the ``EntryCategory`` model class."""
    longMessage = True

    def setUp(self):
        self.obj = EntryCategoryFactory()

    def test_model(self):
        self.assertTrue(self.obj.pk)
