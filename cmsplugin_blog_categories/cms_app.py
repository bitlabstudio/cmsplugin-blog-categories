"""CMS apphook for the ``cmsplugin_blog_categories`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class BlogCategoriesApphook(CMSApp):
    name = _("Blog Categories Apphook")
    urls = ["cmsplugin_blog_categories.urls"]


apphook_pool.register(BlogCategoriesApphook)
