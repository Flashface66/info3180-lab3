from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email
from flask_wtf.csrf import CSRFProtect






class ContactForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    email = StringField('Email',validators=[InputRequired(), Email()])
    subject = StringField('Subject',validators=[InputRequired()])
    message = TextAreaField('Message',validators=[InputRequired()])
    submit = SubmitField('Send')
