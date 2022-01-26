"""Contains configuration data for the flask application.

"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config_Graph():
    """Contains the configuration options for the Dash graphs.

    This class stores the configurable variables for the dash graphs.
    They can be modified inside the settings webpage of the DashOrder project
    and work directly on the graphs.
    """

    graph_data = []
    toggle = False
    font_size_axis = 14
    font_size_legend = 14
    margin_left = 50
    margin_right = 20
    margin_top = 20
    margin_bottom = 50
    x_title = ""
    y_title = ""
