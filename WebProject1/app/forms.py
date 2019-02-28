from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm): #Used for restting password
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class EditProfileForm(FlaskForm): #About me page
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)]) #Length requirement, according to length
    submit = SubmitField('Submit')
    def __init__(self, original_username, *args, **kwargs): 
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username): #report if it has repeat username
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.') #Error Message

class EditPostForm(FlaskForm): #Post Page, maybe error anyway
    name = TextAreaField('Name: ', validators=[
        DataRequired(), Length(min=1, max=40)])
    email = TextAreaField('Email: ', validators=[
        DataRequired(), Length(min=1, max=40)])
    gender = TextAreaField('Gender: ', validators=[
        DataRequired(), Length(min=1, max=40)])
    body = TextAreaField('Enter your post: ', validators=[
        DataRequired(), Length(min=1, max=240)])
    submit = SubmitField('Submit')
    

class PostForm(FlaskForm):
    name = TextAreaField('Name: ', validators=[
        DataRequired(), Length(min=1, max=40)])
    email = TextAreaField('Email: ', validators=[
        DataRequired(), Length(min=1, max=40)])
    gender = TextAreaField('Gender: ', validators=[
        DataRequired(), Length(min=1, max=40)])
    body = TextAreaField('Enter your post: ', validators=[
        DataRequired(), Length(min=1, max=240)])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
