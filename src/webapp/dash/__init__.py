"""Handles the graph page.

The graph page is the main part in DashOrders functionality for the user. A high
configurable graph visualises the users Billbee data in various ways.

Additionaly this subpackage is somehow little special compared to the other webapp subpackages.
Inside this subpackage resides a complete capsulated second flask project, created
with the 'Dash / Plotly' framework. The full sourecode for this exists in the file
'dashexample.py'. See the sourceode to find out more.

The package init file creates the flask blueprint for this subpackage and imports the
flask routes (URL handles).
"""
from flask import Blueprint

bp = Blueprint('dash', __name__)

from webapp.dash import routes  # noqa: E402, F401 isort:skip
