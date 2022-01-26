"""Defines the URL routing for the dash subpackage.

In flask all reachable URLs are defined through decorators.
This file defines the URL route for '/dash'. This route contains
the main users functionality of exploring the dash graph visualisation.

The decorated routing functions contain the logic for what should
happen when the route gets called over HTTP (from a client browser).
In most cases this leads to a return a dynmic created html page via
the flask function 'render_template()'.
"""
from flask import render_template

from webapp.dash import bp, dashexample


@bp.route('/dash')
def dash():
    """Route to the dash graph page.

    Catches the route '/dash' and displays a subpage inside an iframe.
    This route is a bit of a flask-inside-flask trick. The returned template (dash.html)
    contains a fully nested and capsulated flask-website, created with the framework 'Dash / Plotly'.
    The whole dash graph is done with this framework and nested into the outer flask project (this one).
    This 'sub'-flask project gets build inside the file 'dashexample.py' in this package (Dashorder.webapp.dash).
    To learn more about the nested subproject, dive into the sourcecode of 'dashexample.py'.

    Returns:
        'html':
            Nested 'Dash / Plotly' project.

    """
    return render_template(
        'dash/dash.html',
        title='Home',
        dash_url=dashexample.dash_base_url)
