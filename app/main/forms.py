from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, IntegerField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    #name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About')
    submit = SubmitField('Update')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    name = StringField('Item Name:', validators=[Required()])
    destination = StringField('Destination', validators=[Required()])
    quantity = IntegerField('Quantity', validators=[Required()])
    r_email = StringField("Recipient's Email", validators=[Required()])
    id_no = StringField("Recipient ID no.", validators=[Required()])
    phone_no = StringField("Recipient Tel", validators=[Required()])
    body = PageDownField("Other item descriptions?", validators=[Required()])
    status = BooleanField('Shipping status')
    submit = SubmitField('Submit')

class EditPostForm(FlaskForm):
    status=BooleanField('Shipping Status.')
    submit = SubmitField('Confirm')

class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')


class RoutesForm(FlaskForm):
    route_name=StringField('Enter Route name', validators=[Required()])
    start=StringField('Start Point', validators=[Required()])
    city1=StringField('City 1')
    city2=StringField('City 2')
    city3=StringField('City 3')
    city4=StringField('City 4')
    end=StringField('End point', validators=[Required()])
    submit=SubmitField('Create Route')
    
class SearchForm(FlaskForm):
    input_field=StringField("Enter route from above options")
    search=SubmitField("Load route")