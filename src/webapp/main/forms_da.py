"""Form for the Dash graph settings.

User inputs in a flask project are defined through forms.
This class represents the form fields for the Dash graph settings.
"""
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

from Dashorder.webapp import cfg_graph


class DashForm(FlaskForm):
    """Representation of the Input Form for Dash graph configurations.

    This form enables the user to set own configuration options to the
    Dash graph. The form fields are created with WTForms.
    """

    dash_fontsize_axis = RadioField('Graph Schriftgröße Achsen: (14)',
                                    choices=[('12', '12'),
                                             ('14', '14'),
                                             ('16', '16'),
                                             ('18', '18'),
                                             ('20', '20')],
                                    default=cfg_graph.font_size_axis,
                                    validators=[DataRequired()])
    dash_fontsize_legend = RadioField('Graph Schriftgröße Legende: (14)',
                                      choices=[('12', '12'),
                                               ('14', '14'),
                                               ('16', '16'),
                                               ('18', '18'),
                                               ('20', '20')],
                                      default=cfg_graph.font_size_legend,
                                      validators=[DataRequired()])
    dash_margin_left = RadioField('Graph Seitenrand links: (50)',
                                  choices=[('20', '20'),
                                           ('50', '50'),
                                           ('75', '75'),
                                           ('100', '100'),
                                           ('150', '150')],
                                  default=cfg_graph.margin_left,
                                  validators=[DataRequired()])
    dash_margin_right = RadioField('Graph Seitenrand rechts: (20)',
                                   choices=[('20', '20'),
                                            ('50', '50'),
                                            ('75', '75'),
                                            ('100', '100'),
                                            ('150', '150')],
                                   default=cfg_graph.margin_right,
                                   validators=[DataRequired()])
    dash_margin_top = RadioField('Graph Seitenrand oben: (20)',
                                 choices=[('20', '20'),
                                          ('50', '50'),
                                          ('75', '75'),
                                          ('100', '100'),
                                          ('150', '150')],
                                 default=cfg_graph.margin_top,
                                 validators=[DataRequired()])
    dash_margin_bottom = RadioField('Graph Seitenrand unten: (50)',
                                    choices=[('20', '20'),
                                             ('50', '50'),
                                             ('75', '75'),
                                             ('100', '100'),
                                             ('150', '150')],
                                    default=cfg_graph.margin_bottom,
                                    validators=[DataRequired()])
    da_submit = SubmitField('Speichern')
