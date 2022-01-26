"""A complete and capsulated 'Dash / Plotly' Application.

This file contains a full application for the visualisation of the
users Billbee data. It is written in the 'Dash / Plotly' framework, which also
uses flask. This whole 'sub-page' is integrated into the DashOrder flask application
as a single route to '/dash' (internal it is '/dashapp1').

**A little about 'Dash / Plotly':**

All HTML elements have their own classes and constructors (html.H6() or html.Div() i.e.).
Interactive elements like buttons can be bound to callback functions. These callback functions
define their in- and outputs with decorators. Multiple in- and outputs in a single callback are
possible and used here.

The main part of the Dash / Plotly application is a configurable graph-window. This graph gets
its data from requests to the MongoDB (DbHandler), through an abstraction (the statistic package).
Everytime the user clicks the 'show graph' button, the data gets updated and the graph too.

For a better understanding of this part of the DashOrder project, one should play with the
graph and its menu for a while and then come back to the sourcecode here.
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from webapp import cfg_graph

dash_base_url = '/dashapp1/'

def Add_Dash(server) -> None:
    """Create a dash application server and register a flask app to it.

    Inside this function a full dash application is created. It contains the
    dynamic HTML output, serves its own CSS and JS and registers with the outer
    flask app. The content is mostly build by dash HTML classes. The callbacks
    provide the logic for user input.

    Args:
        server (flask application):
            Instance of a flask web application.

    Returns:
        dash application server:
            Instance of a dash application server with the registered flask application.

    """
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    meta_viewport = {"name": "viewport",
                     "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dash_app = dash.Dash(__name__,
                         server=server,
                         url_base_pathname=dash_base_url,
                         external_stylesheets=external_stylesheets,
                         meta_tags=[meta_viewport])

    dash_app.config['suppress_callback_exceptions'] = True

    # -----------------------------------------
    # HTML Layout
    # -----------------------------------------
    with server.app_context():
        dash_app.layout = html.Div(
            [
                html.Div(id="output-clientside"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [html.P("X-Achse:"), html.Div(html.H6("Mlen in Bytes"), id="mini_x")],
                                            id="wells",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.P("Y-Achse:"), html.Div(html.H6("Cycles/Byte"), id="mini_y")],
                                            id="gas",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.P("Graphen:"), html.Div(html.H6("Codebase"), id="mini_g")],
                                            id="oil",
                                            className="mini_container",
                                        ),
                                    ],
                                    id="info-container",
                                    className="row container-display",
                                ),
                                html.Div(style={'height': '590px'}, children=[
                                    dcc.Graph(
                                        id='graph_display',
                                        figure={
                                            'data': cfg_graph.graph_data,
                                            'layout': {
                                                'modebar': {'orientation': 'v'},
                                                'legend': {'orientation': 'h',
                                                           'font': {
                                                                'family': 'sans-serif',
                                                                'size': cfg_graph.font_size_legend,
                                                                'color': 'black'
                                                            }},
                                                'font': {'family': 'sans-serif',
                                                         'size': cfg_graph.font_size_axis,
                                                         'color': 'black'},
                                                'margin': {'l': cfg_graph.margin_left,
                                                           'r': cfg_graph.margin_right,
                                                           't': cfg_graph.margin_top,
                                                           'b': cfg_graph.margin_bottom}},
                                        },
                                        config={
                                            'edits': {
                                                'legendPosition': True,
                                                'legendText': True
                                            },
                                            'toImageButtonOptions': {
                                                'format': 'svg',
                                                'filename': 'custom_image',
                                                'height': 1080,
                                                'width': 1920,
                                                'scale': 1}},
                                        style={'height': 'inherit'})
                                    ],
                                    id="countGraphContainer",
                                    className="pretty_container",
                                ),
                            ],
                            id="right-column",
                            className="nine columns",
                        ),
                    ],
                    className="row flex-display",
                ),
            ],
            id="mainContainer",
            style={"display": "flex", "flex-direction": "column"},
        )

    return dash_app.server
