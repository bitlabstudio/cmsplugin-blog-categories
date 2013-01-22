"""Admin classes for the ``cmsplugin_blog_categories`` app."""
from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from cmsplugin_blog.admin import EntryAdmin
from cmsplugin_blog.models import Entry
from simple_translation.admin import TranslationAdmin
from simple_translation.utils import get_translation_queryset

from cmsplugin_blog_categories.models import Category, EntryCategory


class EntryCategoryInline(admin.TabularInline):
    model = EntryCategory
    max_num = 1


class CustomEntryAdmin(EntryAdmin):
    inlines = [EntryCategoryInline, ]


class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['entry_title', 'category_title', ]

    def category_title(self, obj):
        lang = get_language()
        return get_translation_queryset(obj.category).filter(
            language=lang)[0].title
    category_title.short_description = _('Category')

    def entry_title(self, obj):
        lang = get_language()
        return get_translation_queryset(obj.entry).filter(
            language=lang)[0].title
    entry_title.short_description = _('Entry title')


class CategoryAdmin(TranslationAdmin):
    list_display = ['title', 'languages', ]

    def title(self, obj):
        lang = get_language()
        return get_translation_queryset(obj).filter(language=lang)[0].title
    title.short_description = _('Title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(EntryCategory, EntryCategoryAdmin)
admin.site.unregister(Entry)
admin.site.register(Entry, CustomEntryAdmin)
