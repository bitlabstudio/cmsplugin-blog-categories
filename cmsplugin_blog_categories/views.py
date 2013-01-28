"""Views of the ``cmsplugin_blog_categories`` app."""
from django.views.generic import ListView

from cmsplugin_blog.models import Entry
from cmsplugin_blog_categories.models import Category
from simple_translation.middleware import filter_queryset_language


class CategoryListView(ListView):
    template_name = 'cmsplugin_blog_categories/entry_archive_category.html'
    context_object_name = 'entries'

    def dispatch(self, request, *args, **kwargs):
        self.category = Category.objects.get(slug=kwargs.get('category'))
        return super(CategoryListView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CategoryListView, self).get_context_data(**kwargs)
        ctx.update({'category': self.category, })
        return ctx

    def get_queryset(self):
        qs = Entry.objects.filter(entrycategory__category=self.category)
        qs = filter_queryset_language(self.request, qs)
        return qs
