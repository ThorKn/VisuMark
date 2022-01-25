"""The Dashorder webapp package contains the deployable website of DashOrder.

**In Production Environment:**

Entrypoint for the Website is the file 'application.wsgi', which is a python script
that activates a virtual python environment and creates a flask-application.
The wsgi-script must be called from the HTTP webserver (apache, nginx, etc.).

**In Development Environment:**

The flask application can be instanciated localy be running 'flask run' from a console
in the folder 'webapp' inside a fitting virtual python environment.

**The Website:**

Various flask extensions work together for this website (see setup.py). Mainly the structure is based on
the concept of flask-blueprints. The blueprints are:

* main (indexpage, impressum)
* dash (for the graphs)

Each blueprint appears as a subpackage in the webapp package. Inside the blueprint 'dash'
resides a second framework, the 'Dash / Plotly' visualisation tools.

**Dash / Plotly graphs:**

Dash is a framework to use Plotly graphs inside a website. This is the main feature of
the DashOrder website so far.
The Billbee data gets handled by the packages BbHandler und DbHandler. The Dash graph allows to
analyse and visualise this data via user settings in menues. The result is a individual graph based
on the data and the menu-settings. The graph can be modified interactive and downloaded as an svg-file.

"""
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    """Create the flask website application.

    A flask application gets instanciated and registered with all necessary services,
    databases and configurations.
    These are:

    * Bootstrap framework
    * All flask blueprints

    Returns:
        'flask application':
            A full registered flask application

    """
    app = Flask(__name__)

    bootstrap.init_app(app)

    # Import Flask blueprints
    from webapp.main import bp as main_bp  # isort:skip
    app.register_blueprint(main_bp)

    return app
