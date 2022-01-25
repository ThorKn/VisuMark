"""Defines the URL routing for the main subpackage.

In flask all reachable URLs are defined through decorators.
This file defines the URL routes for the following webpages:

* /index
* /docs
* /einstellungen
* /impressum

The decorated routing functions contain the logic for what should
happen when the route gets called over HTTP (from a client browser).
In most cases this leads to a return a dynmic created html page via
the flask function 'render_template()'.
"""

from flask import flash, render_template

from webapp.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    """Route to the index page.

    Catches the route '/index' and displays a static
    template.

    Returns:
        'html':
            Index page.

    """
    return render_template('main/index.html', title='Home')


@bp.route('/impressum')
def impressum():
    """Route to the impressum page.

    Catches the route '/impressum' and displays a static
    template.

    Returns:
        'html':
            Impressum page.

    """
    return render_template('main/impressum.html', title='Impressum')
