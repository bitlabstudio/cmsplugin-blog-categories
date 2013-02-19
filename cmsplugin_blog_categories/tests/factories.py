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
    title = 'Category Title'
    language = 'en-us'


class CategoryTitleCNFactory(CategoryTitleFactoryBase):
    """Factory for chinese ``CategoryTitle`` objects."""
    title = unichr(34900)
    language = 'zh-cn'


class CategoryPluginFactory(factory.Factory):
    """Base factory for factories for ``CategoryPlugin`` models."""
    FACTORY_FOR = models.CategoryPlugin

    category = factory.SubFactory(CategoryFactory)


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

    category = factory.SubFactory(CategoryFactory)
    entry = factory.SubFactory(EntryFactory)
