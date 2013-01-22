"""Registering translated models for the ``cmsplugin_blog_categories`` app."""
from simple_translation.translation_pool import translation_pool

from cmsplugin_blog_categories.models import Category, CategoryTitle


translation_pool.register_translation(Category, CategoryTitle)
