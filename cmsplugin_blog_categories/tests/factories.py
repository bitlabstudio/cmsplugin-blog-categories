"""
Utilities for creating test objects related to the
``cmsplugin_blog_categories`` app.

"""
from cmsplugin_blog.models import Entry, EntryTitle
import factory

from cmsplugin_blog_categories import models


class CategoryFactory(factory.Factory):
    """Factory for the ``Category`` model."""
    FACTORY_FOR = models.Category

    slug = factory.LazyAttribute(lambda a: 'category-{0}'.format(a))


class CategoryTitleFactoryBase(factory.Factory):
    """Base factory for factories for ``CategoryTitle`` models."""
    FACTORY_FOR = models.CategoryTitle

    category = factory.SubFactory(CategoryFactory)


class CategoryTitleENFactory(CategoryTitleFactoryBase):
    """Factory for english ``CategoryTitle`` objects."""
    title = factory.LazyAttribute(lambda a: 'title-{0}'.format(a))


class EntryFactory(factory.Factory):
    """Base factory for factories for ``Entry`` models."""
    FACTORY_FOR = Entry

    is_published = True


class EntryTitleFactory(factory.Factory):
    """Base factory for factories for ``EntryTitle`` models."""
    FACTORY_FOR = EntryTitle

    entry = factory.SubFactory(EntryFactory)


class EntryCategoryFactory(factory.Factory):
    """Base factory for factories for ``EntryCategory`` models."""
    FACTORY_FOR = models.EntryCategory

    category = factory.SubFactory(CategoryTitleENFactory)
    entry = factory.SubFactory(EntryFactory)
