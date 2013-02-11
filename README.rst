cmsplugin-blog Categories
=========================

An extension for `cmsplugin-blog <https://github.com/fivethreeo/cmsplugin-blog/>`_
which adds categories to the blog. Out of the box cmsplugin-blog only supports
tags.


Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django
    pip install django-cms
    pip install cmsplugin-blog
    pip install simple-translation

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-blog-categories

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-blog-categories.git#egg=cmsplugin_blog_categories

Add ``cmsplugin_blog_categories`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_blog_categories',
    )

In your django-cms instance change the `Blog Apphook` to the `Blog Categories
Apphook`.


Usage
-----

This app includes all URLs of the original cmsplugin-blog, so if you were not
using an apphook but hooked the URLs into your main ``urls.py`` manually,
you should hook this app's ``urls.py`` instead.


Display the category of an entry
++++++++++++++++++++++++++++++++

In order to display an entry's category, do the following::

    {% load cmsplugin_blog_categories_tags %}
    {% get_category entry as category %}
    Category:<a href="{{ category.get_absolute_url }}">{{ category.get_title }}</a>


Display a list of all categories
++++++++++++++++++++++++++++++++

In order to display a list of all available categories, do the following::

    {% load cmsplugin_blog_categories_tags %}
    {% render_category_links exclude_empty=1 %}

Use the ``exclude_empty`` parameter if you want to show only those categories
that have posts.

If you want to control the output of that tag, override the template
`cmsplugin_blog_categories/category_links_snippet.html <https://github.com/bitmazk/cmsplugin-blog-categories/blob/master/cmsplugin_blog_categories/templates/cmsplugin_blog_categories/category_links_snippet.html>`_


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 cmsplugin-blog-categories
    $ pip install -r requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
