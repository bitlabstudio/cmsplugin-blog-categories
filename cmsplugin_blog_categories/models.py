"""Models for the ``cmsplugin_blog_categories`` app."""
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from simple_translation.utils import get_translation_queryset


class Category(models.Model):
    """
    A blog ``Entry`` can belong to one category.

    :slug: The slug for this category. The slug will be the same for all
      languages.

    """
    creation_date = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(
        max_length=512,
        verbose_name=_('Slug'),
    )

    def __unicode__(self):
        return self.get_title()

    @models.permalink
    def get_absolute_url(self):
        return ('blog_archive_category', (), {'category': self.slug, })

    def get_title(self):
        lang = get_language()
        return get_translation_queryset(self).filter(language=lang)[0].title


class CategoryTitle(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
    )

    # Needed by simple-translation
    category = models.ForeignKey(Category)
    language = models.CharField(max_length=5)


class EntryCategory(models.Model):
    """Model that extends the ``Entry`` model of cmsplugin-blog."""
    entry = models.ForeignKey('cmsplugin_blog.Entry')
    category = models.ForeignKey(Category)

    class Meta:
        unique_together = ('entry', 'category', )
