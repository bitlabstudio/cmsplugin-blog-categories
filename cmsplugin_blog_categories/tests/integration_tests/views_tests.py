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


class GetEntriesAjaxViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``GetEntriesAjaxView`` view class."""
    def get_view_name(self):
        return 'blog_get_entries'

    def test_view(self):
        self.should_be_callable_when_anonymous()

    def test_view_with_count(self):
        url = self.get_url()
        url = url + '?count=1'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_view_with_category(self):
        cat_title = CategoryTitleENFactory()
        url = self.get_url()
        url = url + '?category={0}'.format(cat_title.category.slug)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
