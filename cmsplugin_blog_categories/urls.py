"""URLs of the ``cmsplugin_blog_categories`` app. """
from django.conf.urls.defaults import include, patterns, url

from cmsplugin_blog_categories.views import CategoryListView


urlpatterns = patterns(
    '',
    url(r'^category/(?P<category>[^/]*)/',
        CategoryListView.as_view(),
        name='blog_archive_category',),

    url(r'^', include('cmsplugin_blog.urls')),
)
