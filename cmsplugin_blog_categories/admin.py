"""Admin classes for the ``cmsplugin_blog_categories`` app."""
from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from cmsplugin_blog.admin import EntryAdmin
from simple_translation.admin import TranslationAdmin
from simple_translation.utils import get_preferred_translation_from_lang

from cmsplugin_blog_categories.models import Category, EntryCategory


class EntryCategoryInline(admin.TabularInline):
    model = EntryCategory
    extra = 1


class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['entry_title', 'category_title', ]

    def category_title(self, obj):
        """Returns the best available translation for the category title."""
        return obj.category.get_translation().title
    category_title.short_description = _('Category')

    def entry_title(self, obj):
        """Returns the best available translation for the entry title."""
        lang = get_language()
        entry_title = get_preferred_translation_from_lang(obj.entry, lang)
        return entry_title.title
    entry_title.short_description = _('Entry title')


class CategoryAdmin(TranslationAdmin):
    list_display = ['title', 'languages', ]

    def title(self, obj):
        """Returns the best available translation for the catrgory title."""
        return obj.get_translation().title
    title.short_description = _('Title')


# Enhance original EntryAdmin
EntryAdmin.inlines = EntryAdmin.inlines[:] + [EntryCategoryInline]

# Register our own admins
admin.site.register(Category, CategoryAdmin)
admin.site.register(EntryCategory, EntryCategoryAdmin)
