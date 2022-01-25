"""Form for the Billbee update button.

User inputs in a flask project are defined through forms.
This class represents the form field for the Billbee update button.
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField


class UpdateForm(FlaskForm):
    """Representation of the update button Form for gathering Billbee data.

    This form is needed for manual updates from Billbee to DashOrder.
    The form field is created with WTForms.
    """

    bb_update = SubmitField('Update')
