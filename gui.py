from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length

import secrets

from lib.entities import is_there_a_patient_with_this_name
from lib.entities import is_there_a_provider_with_this_name
from lib.json_data_storage import JsonDataStorage
from lib.twilio_messenger import send_sms_message

app = Flask(__name__)

foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)


class SearchForm(FlaskForm):
    patient_first_name = StringField('Patient first name', validators=[DataRequired(), Length(1, 40)])
    patient_last_name = StringField('Patient last name', validators=[DataRequired(), Length(1, 40)])

    provider_first_name = StringField('Provider first name', validators=[DataRequired(), Length(1, 40)])
    provider_last_name = StringField('Provider last name', validators=[DataRequired(), Length(1, 40)])

    submit = SubmitField('Submit')


class AppointmentInformation(FlaskForm):
    appointment_date_time = DateTimeField('time and date', validators=[DataRequired()])
    submit = SubmitField('Submit')
    #send_sms_message(message=f"your appointment has been confirm for {appointment_date_time}")


@app.route('/', methods=['GET', 'POST'])
def index():
    search_form = SearchForm()
    appointment_form = AppointmentInformation()
    message = ""

    if search_form.validate_on_submit():
        valid_patient = is_there_a_patient_with_this_name(first_name=search_form.patient_first_name.data.lower(),
                                                          last_name=search_form.patient_last_name.data.lower(),
                                                          data_storage=JsonDataStorage("lib/test_data.json"))

        valid_provider = is_there_a_provider_with_this_name(first_name=search_form.provider_first_name.data.lower(),
                                                            last_name=search_form.provider_last_name.data.lower(),
                                                            data_storage=JsonDataStorage("lib/test_data.json"))

        patient_message = "" if valid_patient else "Patient is NOT registered"
        provider_message = "" if valid_provider else "Provider is NOT registered"
        message = patient_message + " " + provider_message

        if valid_patient and valid_provider:
            return render_template('appointment.html', appointment_form=appointment_form)

    search_form = SearchForm()
    return render_template('index.html', search_form=search_form, message=message)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4999, debug=True)
