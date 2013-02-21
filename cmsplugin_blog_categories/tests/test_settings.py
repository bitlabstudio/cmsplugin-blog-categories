"""Settings that need to be set in order to run the tests."""
import os

gettext = lambda s: s

DEBUG = True

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = 'cmsplugin_blog_categories.tests.urls'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(__file__, '../../static/')

STATICFILES_DIRS = (
    os.path.join(__file__, 'test_static'),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../templates'),
)

# Settings needed to test a multilingual blog
LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en', gettext('English')),
    ('zh-cn', gettext('Chinese')),
]
USE_I18N = True
USE_L10N = True
CMS_SOFTROOT = True
CMS_PERMISSION = False
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_FRONTEND_LANGUAGES = ('en', 'zh-cn', )
CMS_TEMPLATES = (
    ('cms/home.html', 'Homepage'),
)

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    # cms related apps
    'sekizai',
    'mptt',
    'menus',
    'cms.plugins.text',

    # blog related apps
    'djangocms_utils',
    'simple_translation',
    'tagging',
    'missing',
]

COVERAGE_APPS = [
    # Needed to include cmsplugin_blog_categories, due to their relations
    'cms',
    'cmsplugin_blog',
]

INTERNAL_APPS = [
    'django_nose',
    'cmsplugin_blog_categories.tests.test_app',
    'cmsplugin_blog_categories',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS + COVERAGE_APPS

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), 'coverage')

COVERAGE_MODULE_EXCLUDES = EXTERNAL_APPS + [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions', 'cms$',
    'cmsplugin_blog$',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'simple_translation.middleware.MultilingualGenericsMiddleware',
    'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware',
]


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = (
    'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js')
JQUERY_UI_CSS = (
    'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/'
    'jquery-ui.css')
