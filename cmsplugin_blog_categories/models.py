"""Models for the ``cmsplugin_blog_categories`` app."""
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from simple_translation.utils import get_preferred_translation_from_lang


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

    def get_entries(self):
        """Returns the entries for this category."""
        qs = EntryCategory.objects.select_related()
        qs = qs.filter(
            category=self, entry__is_published=True,
            entry__pub_date__lte=timezone.now())
        qs = qs.order_by('-entry__pub_date')
        return [item.entry for item in qs]

    def get_absolute_url(self):
        url = reverse('blog_archive_category', kwargs={
            'category': self.slug, })
        if 'simple_translation.middleware.MultilingualGenericsMiddleware' in \
                settings.MIDDLEWARE_CLASSES:
            lang = '/{0}'.format(get_language())
            return '{0}{1}'.format(lang, url)
        return '{0}'.format(url)

    def get_title(self):
        return self.get_translation().title

    def get_translation(self):
        lang = get_language()
        return get_preferred_translation_from_lang(self, lang)


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
    entry = models.ForeignKey(
        'cmsplugin_blog.Entry',
        related_name='categories',
        verbose_name=_('Entry'),
    )

    category = models.ForeignKey(
        Category,
        related_name='entry_categories',
        verbose_name=_('Category'),
    )

    class Meta:
        unique_together = ('entry', 'category', )


class CategoryPlugin(CMSPlugin):
    """Plugin, which renders entries belonging to one category."""
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
    )
