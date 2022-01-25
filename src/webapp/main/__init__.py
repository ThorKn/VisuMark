"""Handles the pages main, settings, docs and impressum.

This subpackage handles the following webpages of the DashOrder website:

* main: Startpage with general information about DashOrder (no login required).
* impressum: Legal information about the website (no login required).
* settings: User settings for Billbee, manual Updates and graph configuration (login required).
* docs: Sphinx sourcecode documentation in HTML (login required).

The package init file creates the flask blueprint for this subpackage and imports the
flask routes (URL handles).
"""
from flask import Blueprint

bp = Blueprint('main', __name__, static_folder='static', static_url_path='/docs')

from webapp.main import routes  # noqa: E402, F401 isort:skip
