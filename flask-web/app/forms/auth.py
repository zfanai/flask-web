#encoding:utf8

from flask_babelex import lazy_gettext
from flask_wtf import Form
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import EqualTo
from wtforms.validators import Length

class LoginForm(Form):
    """User login form."""

    username = StringField(lazy_gettext('User'),
                                 description=lazy_gettext('Username or Email'),
                                 validators=[DataRequired(), Length(1, 64)])
    password = PasswordField(lazy_gettext('Password'),
                             description=lazy_gettext('Password'),
                             validators=[DataRequired(), Length(1, 64)])
    remember = BooleanField(lazy_gettext('Keep login'), default=True)
    submit = SubmitField(lazy_gettext('Login'))