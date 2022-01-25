"""Form for the Billbee credentials.

User inputs in a flask project are defined through forms.
This class represents the form fields for the Billbee credentials.
"""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class BillbeeForm(FlaskForm):
    """Representation of the Input Form for Billbee API credentials.

    This form is needed for users Billbee credentials.
    for using the Billbee API a 3-tuple of inormation is needed to
    connect to and request from the Billbee API.
    The form fields are created with WTForms.
    """

    bb_username = StringField('Billbee Benutzername: ', validators=[DataRequired()])
    bb_password = PasswordField('Billbee API Passwort: ', validators=[DataRequired()])
    bb_apikey = StringField('Billbee API Key:      ', validators=[DataRequired()])
    bb_submit = SubmitField('Test und Speichern')
