"""Views of the ``cmsplugin_blog_categories`` app."""
from django.views.generic import ListView

from cmsplugin_blog.models import Entry

from .models import Category


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
        return self.category.get_entries()


class GetEntriesAjaxView(ListView):
    template_name = 'cmsplugin_blog_categories/partials/entry_list.html'
    context_object_name = 'entries'

    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('category'):
            self.category = Category.objects.get(
                slug=request.GET.get('category'))
        else:
            self.category = None
        return super(GetEntriesAjaxView, self).dispatch(
            request, *args, **kwargs)

    def get_queryset(self):
        return Entry.published.all()
