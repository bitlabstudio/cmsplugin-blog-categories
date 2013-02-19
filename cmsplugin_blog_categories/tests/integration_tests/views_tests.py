"""Tests for the views of the ``cmsplugin_blog_categories`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin

from cmsplugin_blog_categories.tests.factories import (
    CategoryTitleENFactory,
    EntryFactory,
)


class CategoryListViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``CategoryListView`` generic view class."""
    def setUp(self):
        self.category_title = CategoryTitleENFactory()
        self.category = self.category_title.category
        self.entry = EntryFactory()

    def get_view_name(self):
        return 'blog_archive_category'

    def get_view_kwargs(self):
        return {'category': self.category.slug}

    def test_view(self):
        self.should_be_callable_when_anonymous()
